-- SELECT name FROM sqlite_schema WHERE type='table'; -- get all tables

-- DROP OLD TABLES

DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS referee;
DROP TABLE IF EXISTS control;
DROP TABLE IF EXISTS stat;
DROP TABLE IF EXISTS team;
DROP TABLE IF EXISTS match;
DROP TABLE IF EXISTS participation;

-- CREATE TABLES

PRAGMA foreign_keys = ON; -- ENABLE FOREIGN KEYS

--People
CREATE TABLE IF NOT EXISTS people(people_id TEXT NOT NULL PRIMARY KEY,
name TEXT, surname TEXT, birthdate DATE, tel TEXT, nationality TEXT);

--Player
CREATE TABLE IF NOT EXISTS player(player_id TEXT NOT NULL PRIMARY KEY,
person_id TEXT, team_name TEXT,
position TEXT,
FOREIGN KEY (people_id) REFERENCES people(people_id),
FOREIGN KEY (team_name) REFERENCES team(team_name)
);

--Referee
CREATE TABLE IF NOT EXISTS referee(referee_id TEXT NOT NULL PRIMARY KEY,
people_id TEXT, position TEXT,
FOREIGN KEY (person_id) REFERENCES people(people_id)
);

--Control = Diefthinseis Agwnwn
CREATE TABLE IF NOT EXISTS control(match_id INTEGER NOT NULL,
referee_id TEXT,
FOREIGN KEY (match_id) REFERENCES match(match_id),
FOREIGN KEY (referee_id) REFERENCES referee(referee_id)
);

--Statistics
CREATE TABLE IF NOT EXISTS stat(statistics_id INTEGER NOT NULL PRIMARY KEY,
player_id TEXT, match_id INTEGER,
minute INTEGER, stat_name TEXT,
FOREIGN KEY (player_id) REFERENCES player(player_id),
FOREIGN KEY (match_id) REFERENCES match(match_id)
);

--team
CREATE TABLE IF NOT EXISTS team(team_name TEXT NOT NULL PRIMARY KEY,
home TEXT, founded DATE);

--Matches
CREATE TABLE IF NOT EXISTS match(match_id INTEGER NOT NULL PRIMARY KEY,
datime DATETIME, home_goals INTEGER, away_goals INTEGER);

--Participation
CREATE TABLE IF NOT EXISTS participation(
match_id INTEGER NOT NULL PRIMARY KEY,
home_team TEXT NOT NULL, away_team TEXT NOT NULL,
FOREIGN KEY (match_id) REFERENCES match(id),
FOREIGN KEY (home_team) REFERENCES team(team_name),
FOREIGN KEY (away_team) REFERENCES team(team_name)
);


-- INSERT INPUTS
INSERT INTO people VALUES
('AN123456',  'John', 'Pipas', DATE('2001-11-20'), '+306918273645', 'Albanian');
INSERT INTO people VALUES
('AM987654',  'Julian', 'Koulevski', DATE('1989-05-13'), '6946875120', 'French');

INSERT INTO team VALUES ('Panatha', 'Athens', DATE('1908-02-03'));
INSERT INTO team VALUES ('PAOK', 'Salonica', DATE('1926-04-20'));
INSERT INTO team VALUES ('ARIS', 'Salonica', DATE('1914-03-25'));

INSERT INTO match (datime, home_goals, away_goals) VALUES (DATETIME('2022-02-03 21:00'), 2,1 );
INSERT INTO participation (home_team, away_team) VALUES ('Panatha', 'PAOK');

INSERT INTO match (datime, home_goals, away_goals) VALUES (DATETIME('2022-02-23 20:30'), 0,1 );
INSERT INTO participation (home_team, away_team) VALUES ('ARIS', 'PAOK');

INSERT INTO match (datime, home_goals, away_goals) VALUES (DATETIME('2022-03-05 21:30'), 1,0 );
INSERT INTO participation (home_team, away_team) VALUES ('Panatha', 'ARIS');

INSERT INTO player VALUES ('PL1', 'AN123456', 'Panatha', 'CF');
INSERT INTO referee VALUES ('REF1', 'AM987654', 'pos1');

INSERT INTO control VALUES (1,'REF1');
INSERT INTO control VALUES (2,'REF1');
INSERT INTO control VALUES (3,'REF1');

INSERT INTO stat (player_id, match_id, minute, stat_name) VALUES ('PL1', 1, 69, 'goal');
INSERT INTO stat (player_id, match_id, minute, stat_name) VALUES ('PL1', 1, 70, 'foul');
INSERT INTO stat (player_id, match_id, minute, stat_name) VALUES ('PL1', 1, 71, 'offside');
INSERT INTO stat (player_id, match_id, minute, stat_name) VALUES ('PL1', 2, 69, 'goal');

