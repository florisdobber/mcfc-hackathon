DROP TABLE IF EXISTS team_data;
DROP TABLE IF EXISTS match_data;
DROP TABLE IF EXISTS player_data;
DROP TABLE IF EXISTS lineup_data;
DROP TABLE IF EXISTS goal_data;

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
  position VARCHAR(255),
  start_time INTEGER,
  start_period INTEGER,
  start_reason VARCHAR(255),
  end_time INTEGER,
  end_period INTEGER,
  end_reason VARCHAR(255),
  position_number INTEGER,
  PRIMARY KEY (match_id, team_id, player_id, position_number),
  CONSTRAINT fk_lineup_match
    FOREIGN KEY (match_id)
    REFERENCES match_data(id),
  CONSTRAINT fk_lineup_team
    FOREIGN KEY (team_id)
    REFERENCES team_data(id),
  CONSTRAINT fk_lineup_player
    FOREIGN KEY (player_id)
    REFERENCES player_data(id)
);

CREATE TABLE goal_data (
  id VARCHAR(255),
  match_id INTEGER,
  team_id INTEGER,
  player_id INTEGER,
  time INTEGER,
  own_goal BOOLEAN,
  PRIMARY KEY (id),
  CONSTRAINT fk_goal_match
    FOREIGN KEY (match_id)
    REFERENCES match_data(id),
  CONSTRAINT fk_goal_team
    FOREIGN KEY (team_id)
    REFERENCES team_data(id),
  CONSTRAINT fk_goal_player
    FOREIGN KEY (player_id)
    REFERENCES player_data(id)
);