from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('match', __name__, url_prefix='/match')

@bp.route('/', methods=['GET'])
def match():    
    return render_template('match.html')