import os
import random

from flask import Flask, render_template, jsonify, request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/sub_recs', methods=['POST'])
    def sub_recs():
        time = int(request.json['time'])
        lineup = request.json['lineup']
        subs = request.json['subs']
        
        random.seed(time)
        
        # Pick 3 random players from both sides
        out_subs = random.sample(lineup, k=3)
        in_subs = random.sample(subs, k=3)
        
        # Create object
        recommended_subs = [
            {
                'out_jersey_number': out_subs[i]['jersey_number'],
                'out_name': out_subs[i]['name'],
                'time': random.randint(max(int(time / 60), 60), 90),
                'in_jersey_number': in_subs[i]['jersey_number'],
                'in_name': in_subs[i]['name'],
            } 
            for i 
            in range(3)
        ]
        
        return jsonify(recommended_subs)
    
    from . import db
    db.init_app(app)
    
    from . import home
    app.register_blueprint(home.bp)
    
    from . import match
    app.register_blueprint(match.bp)

    return app