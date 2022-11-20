
-- DROP OLD TABLES

DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS clubs;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS partitipations;

-- CREATE TABLES

CREATE TABLE IF NOT EXISTS people(id TEXT NOT NULL PRIMARY KEY,
name TEXT, surname TEXT, birthdate DATE, address TEXT, tel TEXT, nationality TEXT);
CREATE TABLE IF NOT EXISTS clubs(name TEXT NOT NULL PRIMARY KEY,
home TEXT, founded DATE);
CREATE TABLE IF NOT EXISTS matches(id INTEGER NOT NULL PRIMARY KEY,
date DATE, home_team_goals INTEGER, visiting_team_goals INTEGER);

PRAGMA foreign_keys = ON; -- ENABLE FOREIGN KEYS

CREATE TABLE IF NOT EXISTS partitipations(match INTEGER NOT NULL,
	FOREIGN KEY(match) REFERENCES matches(id));


-- INSERT INPUTS
INSERT INTO people VALUES
('AN123456',  'Pigos', 'Pepas', DATE('2001-11-20'), 'Thali 23, Patras, Greece', '+306918273645', 'Albanian');
INSERT INTO clubs VALUES ('Panatha', 'Athens', DATE('1908-02-03'));
INSERT INTO matches (date, home_team_goals, visiting_team_goals) VALUES (DATE('1908-02-03'), 2,1 );