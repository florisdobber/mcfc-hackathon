import os
import json
import pandas as pd

player_data = []

directory_path = os.path.join('data', 'StatsBomb', 'Data')

for filename in os.listdir(directory_path):
    if filename.startswith('ManCity_') and filename.endswith('_lineups.json'):
        # Open the JSON file
        with open(os.path.join(directory_path, filename), 'r') as f:
            data = json.load(f)

        for team in data:
            team_id = team["team_id"]
            for player in team["lineup"]:
                player_id = player["player_id"]
                player_name = player["player_nickname"] if player["player_nickname"] != None else player["player_name"]
                jersey_number = player["jersey_number"]

                player_data.append({
                    "id": player_id,
                    "name": player_name,
                    "jersey_number": jersey_number,
                    "team_id":team_id
                })

df = pd.DataFrame(player_data).drop_duplicates()

df.to_csv('data-processed/player_data.csv', index=False)