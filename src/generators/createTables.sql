-- FLUSH DATABASE

DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS team;
DROP TABLE IF EXISTS match;
DROP TABLE IF EXISTS participation;
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS referee;
DROP TABLE IF EXISTS control;
DROP TABLE IF EXISTS statistic;


-- CREATE TABLES

PRAGMA foreign_keys = ON; -- ENABLE FOREIGN KEYS

-- People
CREATE TABLE IF NOT EXISTS people(
    people_id CHAR(8) NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    birthdate DATE,
    tel CHAR(14),
    nationality TEXT
);

-- Player
CREATE TABLE IF NOT EXISTS player(
    player_id CHAR(10) NOT NULL PRIMARY KEY,
    people_id CHAR(8) NOT NULL,
    team_name TEXT,
    position VARCHAR(3),
    FOREIGN KEY(people_id) REFERENCES people(people_id),
    FOREIGN KEY(team_name) REFERENCES team(team_name)
);

-- Referee
CREATE TABLE IF NOT EXISTS referee(
    referee_id CHAR(10) NOT NULL PRIMARY KEY,
    people_id CHAR(8) NOT NULL,
    type TEXT,
    FOREIGN KEY(people_id) REFERENCES people(people_id)
);

-- Team
CREATE TABLE IF NOT EXISTS team(
    team_name TEXT NOT NULL PRIMARY KEY,
    home TEXT,
    founded DATE
);

-- Match
CREATE TABLE IF NOT EXISTS match(
    match_id INTEGER NOT NULL PRIMARY KEY,
    datime DATETIME,
    home_team_goals INTEGER,
    away_team_goals INTEGER
);

-- Participation
CREATE TABLE IF NOT EXISTS participation(
    match_id INTEGER NOT NULL,
    home_team TEXT NOT NULL,
    away_team TEXT NOT NULL,
    PRIMARY KEY (match_id),
    FOREIGN KEY (match_id) REFERENCES match(match_id),
    FOREIGN KEY (home_team) REFERENCES team(team_name),
    FOREIGN KEY (away_team) REFERENCES team(team_name)
);

-- Match-Control by Referee
CREATE TABLE IF NOT EXISTS control(
    match_id INTEGER NOT NULL,
    referee_id CHAR(10) NOT NULL,
    FOREIGN KEY(match_id) REFERENCES match(match_id),
    FOREIGN KEY(referee_id) REFERENCES referee(referee_id)
);

-- Statistics
CREATE TABLE IF NOT EXISTS statistic(
    statistic_id INTEGER NOT NULL PRIMARY KEY,
    match_id INTEGER NOT NULL,
    player_id CHAR(10),
    minute INTEGER,
    stat_name TEXT,
    FOREIGN KEY(match_id) REFERENCES match(match_id),
    FOREIGN KEY(player_id) REFERENCES player(player_id)
);


-- INSERT INPUTS
---



