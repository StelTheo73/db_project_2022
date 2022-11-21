-- SELECT name FROM sqlite_schema WHERE type='table'; -- get all tables

-- DROP OLD TABLES

DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS referees;
DROP TABLE IF EXISTS controls;
DROP TABLE IF EXISTS stats;
DROP TABLE IF EXISTS clubs;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS participations;

-- CREATE TABLES

PRAGMA foreign_keys = ON; -- ENABLE FOREIGN KEYS

--People
CREATE TABLE IF NOT EXISTS people(id TEXT NOT NULL PRIMARY KEY,
name TEXT, surname TEXT, birthdate DATE, address TEXT, tel TEXT, nationality TEXT);

--Players
CREATE TABLE IF NOT EXISTS players(player_id TEXT NOT NULL PRIMARY KEY,
person_id TEXT, club TEXT,
position TEXT,
FOREIGN KEY (person_id) REFERENCES people(id),
FOREIGN KEY (club) REFERENCES clubs(name)
);

--Referees
CREATE TABLE IF NOT EXISTS referees(referee_id TEXT NOT NULL PRIMARY KEY,
person_id TEXT, position TEXT,
FOREIGN KEY (person_id) REFERENCES people(id)
);

--Controls = Diefthinseis Agwnwn
CREATE TABLE IF NOT EXISTS controls(match_id INTEGER NOT NULL PRIMARY KEY,
referee_id TEXT,
FOREIGN KEY (match_id) REFERENCES matches(id),
FOREIGN KEY (referee_id) REFERENCES referees(referee_id)
);

--Statistics
CREATE TABLE IF NOT EXISTS stats(statistics_id INTEGER NOT NULL PRIMARY KEY,
player_id TEXT, match_id INTEGER,
minute INTEGER, stat_name TEXT,
FOREIGN KEY (player_id) REFERENCES players(player_id),
FOREIGN KEY (match_id) REFERENCES matches(id)
);

--Clubs
CREATE TABLE IF NOT EXISTS clubs(name TEXT NOT NULL PRIMARY KEY,
home TEXT, founded DATE);

--Matches
CREATE TABLE IF NOT EXISTS matches(id INTEGER NOT NULL PRIMARY KEY,
date DATE, home_team_goals INTEGER, visiting_team_goals INTEGER);

--Participations
CREATE TABLE IF NOT EXISTS participations(
match_id INTEGER NOT NULL PRIMARY KEY,
home_team TEXT NOT NULL, away_team TEXT NOT NULL,
FOREIGN KEY (match_id) REFERENCES matches(id),
FOREIGN KEY (home_team) REFERENCES clubs(name),
FOREIGN KEY (away_team) REFERENCES clubs(name)
);


-- INSERT INPUTS
INSERT INTO people VALUES
('AN123456',  'John', 'Pipas', DATE('2001-11-20'), 'Thali 23, Patras, Greece', '+306918273645', 'Albanian');
INSERT INTO people VALUES
('AM987654',  'Jack', 'Kalos', DATE('1989-05-13'), 'Zaimi 2, Patras, Greece', '6946875120', 'French');

INSERT INTO clubs VALUES ('Panatha', 'Athens', DATE('1908-02-03'));
INSERT INTO clubs VALUES ('PAOK', 'Salonica', DATE('1926-04-20'));
INSERT INTO clubs VALUES ('ARIS', 'Salonica', DATE('1914-03-25'));

INSERT INTO matches (date, home_team_goals, visiting_team_goals) VALUES (DATE('2022-02-03'), 2,1 );
INSERT INTO participations (home_team, away_team) VALUES ('Panatha', 'PAOK');

INSERT INTO matches (date, home_team_goals, visiting_team_goals) VALUES (DATE('2022-02-23'), 0,1 );
INSERT INTO participations (home_team, away_team) VALUES ('ARIS', 'PAOK');

INSERT INTO matches (date, home_team_goals, visiting_team_goals) VALUES (DATE('2022-03-05'), 1,0 );
INSERT INTO participations (home_team, away_team) VALUES ('Panatha', 'ARIS');

INSERT INTO players VALUES ('PL1', 'AN123456', 'Panatha', 'CF');
INSERT INTO referees VALUES ('REF1', 'AM987654', 'pos1');

INSERT INTO controls VALUES (1,'REF1');
INSERT INTO controls VALUES (2,'REF1');
INSERT INTO controls VALUES (3,'REF1');

INSERT INTO stats (player_id, match_id, minute, stat_name) VALUES ('PL1', 1, 69, 'goal');
INSERT INTO stats (player_id, match_id, minute, stat_name) VALUES ('PL1', 1, 70, 'foul');
INSERT INTO stats (player_id, match_id, minute, stat_name) VALUES ('PL1', 1, 71, 'offside');
INSERT INTO stats (player_id, match_id, minute, stat_name) VALUES ('PL1', 2, 69, 'goal');

