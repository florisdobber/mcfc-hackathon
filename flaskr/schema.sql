DROP TABLE IF EXISTS team_data;
DROP TABLE IF EXISTS match_data;
DROP TABLE IF EXISTS player_data;
DROP TABLE IF EXISTS lineup_data;

CREATE TABLE team_data (
  id INT PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE match_data (
  match_id INTEGER PRIMARY KEY,
  home_team_id INTEGER,
  away_team_id INTEGER,
  CONSTRAINT fk_team_match_home
    FOREIGN KEY (home_team_id)
    REFERENCES team_data(id),
  CONSTRAINT fk_team_match_away 
    FOREIGN KEY (away_team_id)
    REFERENCES team_data(id)
);

CREATE TABLE player_data (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  jersey_number INT,
  team_id INT,
  CONSTRAINT fk_team_player
    FOREIGN KEY (team_id)
    REFERENCES team_data(id)
);

CREATE TABLE lineup_data (
  match_id INTEGER,
  team_id INTEGER,
  player_id INTEGER,
  `on` INTEGER,  -- TODO: Adjust data type
  off INTEGER,  -- TODO: Adjust data type
  reason VARCHAR(255),
  PRIMARY KEY (match_id, team_id, player_id),
  CONSTRAINT fk_lineup_match
    FOREIGN KEY (match_id)
    REFERENCES match_data(id),
  CONSTRAINT fk_lineup_team
    FOREIGN KEY (team_id)
    REFERENCES team_data(id),
  CONSTRAINT fk_lineup_player
    FOREIGN KEY (team_id)
    REFERENCES team_data(id)
);