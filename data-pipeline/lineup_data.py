import os
import json
import numpy as np
import pandas as pd
from datetime import datetime

def time_to_seconds(time_str):
    if time_str is None:
        return None
    
    time_format = "%H:%M:%S.%f"
    parsed_time = datetime.strptime(time_str, time_format)

    hours = parsed_time.hour
    minutes = parsed_time.minute
    seconds = parsed_time.second
    milliseconds = parsed_time.microsecond / 1000

    total_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000
    return round(total_seconds, 3)

lineup_data = []

directory_path = os.path.join('data', 'StatsBomb', 'Data')

for filename in os.listdir(directory_path):
    if filename.startswith('ManCity_') and filename.endswith('_lineups.json'):
        # Open the JSON file
        with open(os.path.join(directory_path, filename), 'r') as f:
            data = json.load(f)

        #set for home matches
        if 'Arsenal' in filename:
            match_id = 3852832
            #home: 3852832
            #away: 3856060
        elif 'AstonVilla' in filename:
            match_id = 3856030
            #home: 3856030
            #away: 3852839
        elif 'Brighton' in filename:
            match_id = 3855980
            #home: 3855980
            #away: 3856046
        elif 'LeicesterCity' in filename:
            match_id = 3855947
            #home: 3855947
            #away: 3856033
        elif 'Liverpool' in filename:
            match_id = 3855961
            #home: 3855961
            #away: 3856074
        elif 'Tottenham' in filename:
            match_id = 3856040
            #home: 3856040
            #away: 3855954

        for team in data:
            team_id = team["team_id"]
            
            for player in team["lineup"]:
                position_counter = 0
                
                if len(player['positions']) == 0:
                    lineup_data.append({
                        "match_id": match_id,
                        "team_id": team_id,
                        "player_id": player["player_id"],
                        "position": None,
                        "start_time": None,
                        "start_period": None,
                        "start_reason": None,
                        "end_time": None,
                        "end_period": None,
                        "end_reason": None,
                        "position_number": 0
                    })
                else:
                    for item in player["positions"]:
                        position_counter += 1
                        lineup_data.append({
                            "match_id": match_id,
                            "team_id": team_id,
                            "player_id": player["player_id"],
                            "position": item["position"],
                            "start_time": time_to_seconds(item["from"]),
                            "start_period": item["from_period"],
                            "start_reason": item["start_reason"],
                            "end_time": time_to_seconds(item["to"]),
                            "end_period": item["to_period"],
                            "end_reason": item["end_reason"],
                            "position_number": position_counter
                        })

df = pd.DataFrame(lineup_data).drop_duplicates()

df.to_csv('data-processed/lineup_data.csv', index=False, na_rep='')