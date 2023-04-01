import json
import pandas as pd

# Read in the data
with open('data\statsbomb\FAWSL_22_23.json', 'r') as f:
    data = json.load(f)

# Extract the required information
match_data = []
for item in data:
    match_id = item["match_id"]
    home_team_name = item["home_team"]["home_team_name"]
    away_team_name = item["away_team"]["away_team_name"]
    match_data.append({
        "match_id": match_id,
        "home_team_name": home_team_name,
        "away_team_name": away_team_name
    })

# Create a Pandas dataframe
df = pd.DataFrame(match_data)

df.to_csv('data-processed/match_data.csv', index=False)