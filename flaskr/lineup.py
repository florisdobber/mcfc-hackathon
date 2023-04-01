import functools
import pandas as pd

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('lineup', __name__, url_prefix='/lineup')

@bp.route('/', methods=['GET'])
def home():
    db = get_db()
    
    query = """SELECT * FROM match_data WHERE home_team_name = 'Manchester City WFC' OR away_team_name = 'Manchester City WFC'"""
    data = db.execute(query).fetchall()
    
    return render_template('index.html', data=data)