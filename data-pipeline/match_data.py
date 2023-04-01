import os
import json
import pandas as pd

# Read in the data
with open(os.path.join('data', 'StatsBomb', 'Data', 'FAWSL_22_23.json'), 'r') as f:
    data = json.load(f)

# Extract the required information
match_data = []
for item in data:
    match_id = item["match_id"]
    home_team_id = item["home_team"]["home_team_id"]
    away_team_id = item["away_team"]["away_team_id"]
    match_data.append({
        "match_id": match_id,
        "home_team_id": home_team_id,
        "away_team_id": away_team_id
    })

# Create a Pandas dataframe
df = pd.DataFrame(match_data)

df.to_csv(os.path.join('data-processed', 'match_data.csv'), index=False)