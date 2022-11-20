
-- DROP OLD TABLES

DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS clubs;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS participations;

-- CREATE TABLES

CREATE TABLE IF NOT EXISTS people(id TEXT NOT NULL PRIMARY KEY,
name TEXT, surname TEXT, birthdate DATE, address TEXT, tel TEXT, nationality TEXT);
CREATE TABLE IF NOT EXISTS clubs(name TEXT NOT NULL PRIMARY KEY,
home TEXT, founded DATE);
CREATE TABLE IF NOT EXISTS matches(id INTEGER NOT NULL PRIMARY KEY,
date DATE, home_team_goals INTEGER, visiting_team_goals INTEGER);

PRAGMA foreign_keys = ON; -- ENABLE FOREIGN KEYS

CREATE TABLE IF NOT EXISTS participations(
match INTEGER NOT NULL, 
team1 TEXT NOT NULL,
team2 TEXT NOT NULL,
FOREIGN KEY(match) REFERENCES matches(id),
FOREIGN KEY(team1) REFERENCES clubs(name),
FOREIGN KEY(team2) REFERENCES clubs(name)
);


-- INSERT INPUTS
INSERT INTO people VALUES
('AN123456',  'Pigos', 'Pepas', DATE('2001-11-20'), 'Thali 23, Patras, Greece', '+306918273645', 'Albanian');
INSERT INTO clubs VALUES ('Panatha', 'Athens', DATE('1908-02-03'));
INSERT INTO clubs VALUES ('PAOK', 'Salonica', DATE('1938-12-09'));
INSERT INTO matches (date, home_team_goals, visiting_team_goals) VALUES (DATE('1908-02-03'), 2,1 );

INSERT INTO participations VALUES (1, 'Panatha', 'PAOK');

