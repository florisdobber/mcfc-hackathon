import os
import json
import pandas as pd

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
                player_id = player["player_id"]
                position_counter = 0
                for item in player["positions"]:
                    position_counter += 1
                    position = item["position"]
                    start_time = item["from"]
                    start_period = item["from_period"]
                    start_reason = item["start_reason"]
                    end_time = item["to"]
                    end_period = item["to_period"]
                    end_reason = item["end_reason"]

                    lineup_data.append({
                        "match_id": match_id,
                        "team_id": team_id,
                        "player_id": player_id,
                        "position": position,
                        "start_time": start_time,
                        "start_period": start_period,
                        "start_reason": start_reason,
                        "end_time": end_time,
                        "end_period": end_period,
                        "end_reason": end_reason,
                        "position_number": position_counter
                    })

df = pd.DataFrame(lineup_data).drop_duplicates()

df.to_csv('data-processed/lineup_data.csv', index=False)