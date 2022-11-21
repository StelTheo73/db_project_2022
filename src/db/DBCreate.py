## IMPORTANT: Run while in folder 'DB_PROJECT_2022' (for the paths)

import sqlite3, os
DB_PATH = './src/db/database.db'
SQL_PATH = './src/db/DBCreationScript.sql'

# DELETE ALL DATABASE for initialization purposes
if os.path.exists(DB_PATH): os.remove(DB_PATH)

# CREATE AND CONNECT DB
db = sqlite3.connect(DB_PATH)

def manually_createdb(): #deprecated
    # DROP OLD TABLES

    db.execute("DROP TABLE IF EXISTS people")
    db.execute("DROP TABLE IF EXISTS clubs")
    db.execute("DROP TABLE IF EXISTS matches")
    db.execute("DROP TABLE IF EXISTS partitipations")


    # CREATE TABLES

    db.execute("CREATE TABLE IF NOT EXISTS people(\
    	id TEXT NOT NULL PRIMARY KEY,\
    	name TEXT, surname TEXT, birthdate DATE, address TEXT, tel TEXT, nationality TEXT)")

    db.execute("CREATE TABLE IF NOT EXISTS clubs(\
    	name TEXT NOT NULL PRIMARY KEY,\
    	home TEXT, founded DATE)")

    db.execute("CREATE TABLE IF NOT EXISTS matches(\
    	id INTEGER NOT NULL PRIMARY KEY,\
    	date DATE, home_team_goals INTEGER, visiting_team_goals INTEGER)")

    db.execute("PRAGMA foreign_keys = ON")

    db.execute("CREATE TABLE IF NOT EXISTS partitipations(\
        match INTEGER NOT NULL,\
    	FOREIGN KEY(match) REFERENCES matches(id)\
        )")



    # TEST INPUTS

    db.execute("INSERT INTO people VALUES ('AN123456',  'Pigos', 'Pepas', DATE('2001-11-20'), 'Thali 23, Patras, Greece', '+306918273645', 'Albanian')")
    db.execute("INSERT INTO clubs VALUES ('Panatha', 'Athens', DATE('1908-02-03'))")
    db.execute("INSERT INTO matches (date, home_team_goals, visiting_team_goals) VALUES (DATE('1908-02-03'), 2,1 )")


# EXECUTE THE EXTERNAL SQL SCRIPT

with open(SQL_PATH, 'r') as sql_file:
    db.executescript(sql_file.read())

db.commit()


# TEST OUTPUTS

print("\nPeople:")
[print(person) for person in db.execute("SELECT * FROM people")]
print("\nPlayers:")
[print(player) for player in db.execute("SELECT * FROM players")]
print("\nReferees:")
[print(referee) for referee in db.execute("SELECT * FROM referees")]
print("\nMatch Controls by refs:")
[print(control) for control in db.execute("SELECT * FROM controls")]
print("\nPlayers' Statistics:")
[print(stat) for stat in db.execute("SELECT * FROM stats")]
print("\nClubs:")
[print(club) for club in db.execute("SELECT * FROM clubs")]
print("\nMatches:")
[print(match) for match in db.execute("SELECT * FROM matches")]
print("\nParticipations:")
[print(participation) for participation in db.execute("SELECT * FROM participations")]


db.close()
