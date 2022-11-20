import sqlite3

db = sqlite3.connect('./src/db/database.db')

def manually_createdb():
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

with open('./src/db/DBCreationScript.sql', 'r') as sql_file:
    db.executescript(sql_file.read())

db.commit()

# TEST OUTPUTS

print("People:")
[print(person) for person in db.execute("SELECT * FROM people")]
print("Clubs:")
[print(club) for club in db.execute("SELECT * FROM clubs")]
print("Matches:")
[print(match) for match in db.execute("SELECT * FROM matches")]
print("Participations:")
[print(match) for match in db.execute("SELECT * FROM participations")]

db.close()
