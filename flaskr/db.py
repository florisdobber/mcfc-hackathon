import sqlite3
import csv
import os

import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()



def load_data(file_name):
    db = get_db()
    
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(root_dir, 'data-processed', file_name + '.csv')
    
    
    with open(file_path, 'r') as file_data:
        reader = csv.DictReader(file_data)
        
        columns = ', '.join(reader.fieldnames)
        question_marks = ', '.join(['?' for x in reader.fieldnames])
        
        for row in reader:
            db.execute(
                f"INSERT INTO {file_name} ({columns}) VALUES ({question_marks})", tuple(row.values())
            )
    
    db.commit()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
        
    load_data('match_data')
    load_data('team_data')


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)