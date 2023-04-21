import os
import json
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

directory_path = os.path.join('data', 'StatsBomb', 'Data')

goal_data = []

for filename in os.listdir(directory_path):
    if filename.endswith('_events.json'):
        # Open the JSON file
        with open(os.path.join(directory_path, filename), 'r') as f:
            data = json.load(f)
        
        #set for home matches
        if 'Arsenal' in filename:
            match_id = 3852832
        elif 'AstonVilla' in filename:
            match_id = 3856030
        elif 'Brighton' in filename:
            match_id = 3855980
        elif 'LeicesterCity' in filename:
            match_id = 3855947
        elif 'Liverpool' in filename:
            match_id = 3855961
        elif 'Tottenham' in filename:
            match_id = 3856040

        for event in data:
            if event.get('shot', {}).get('outcome', {}).get('name', {}) == "Goal":
                goal_data.append({
                    'id': event['id'],
                    'match_id': match_id,
                    'team_id': event['team']['id'],
                    'player_id': event['player']['id'],
                    'time': time_to_seconds(event['timestamp']),
                    'own_goal': False
                })
            
            elif event.get('type', {}).get('name', {}) == 'Own Goal Against':
                goal_data.append({
                    'id': event['id'],
                    'match_id': match_id,
                    'team_id': event['possession_team']['id'],
                    'player_id': event['player']['id'],
                    'time': time_to_seconds(event['timestamp']),
                    'own_goal': True
                })

df = pd.DataFrame(goal_data)

df.to_csv('data-processed/goal_data.csv', index=False)