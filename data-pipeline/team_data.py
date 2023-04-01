import os
import json
import pandas as pd

# Read in the data
with open(os.path.join('data', 'StatsBomb', 'Data', 'FAWSL_22_23.json'), 'r') as f:
    data = json.load(f)

# Extract the required information
team_data = []

for item in data:
    home_team_id = item["home_team"]["home_team_id"]
    home_team_name = item["home_team"]["home_team_name"]
    away_team_id = item["away_team"]["away_team_id"]
    away_team_name = item["away_team"]["away_team_name"]

    team_data.append({
        "id": home_team_id,
        "name": home_team_name,
    })

    team_data.append({
        "id": away_team_id,
        "name": away_team_name
    })

# Create a Pandas dataframe
df = pd.DataFrame(team_data).drop_duplicates()

df.to_csv(os.path.join('data-processed', 'team_data.csv'), index=False)