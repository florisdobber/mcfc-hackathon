from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('home', __name__, url_prefix='')

@bp.route('/', methods=['GET'])
def home():
    db = get_db()
    
    query = """
        SELECT 
            match_data.match_id, 
            home_team.name AS home_team_name,
            away_team.name AS away_team_name
        FROM match_data
        LEFT JOIN team_data AS home_team
            ON match_data.home_team_id = home_team.id
        LEFT JOIN team_data AS away_team
            ON match_data.away_team_id = away_team.id
        WHERE match_data.match_id IN (3852832, 3856030, 3855980, 3855947, 3855961, 3856040)
        """
    data = db.execute(query).fetchall()
    
    return render_template('home.html', data=data)