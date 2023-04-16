from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('match', __name__, url_prefix='/match')

@bp.route('/<match_id>', methods=['GET'])
@bp.route('/<match_id>/<int:minute>', methods=['GET'])
def match(match_id, minute=0):
    db = get_db()
    
    query = f"""
        SELECT 
            match_data.match_id, 
            home_team.name AS home_team_name,
            away_team.name AS away_team_name
        FROM match_data
        LEFT JOIN team_data AS home_team
            ON match_data.home_team_id = home_team.id
        LEFT JOIN team_data AS away_team
            ON match_data.away_team_id = away_team.id
        WHERE match_data.match_id = {match_id}
        """
    match_data = db.execute(query).fetchone()
    
    query = f"""
        SELECT
            player_data.id AS player_id,
            player_data.name,
            player_data.jersey_number,
            lineup_data.position
        FROM lineup_data
        LEFT JOIN player_data
            ON lineup_data.player_id = player_data.id
        WHERE lineup_data.match_id = {match_id}
        """
    lineup_data = db.execute(query).fetchall()
    
    return render_template('match.html', match_data=match_data, lineup_data=lineup_data)