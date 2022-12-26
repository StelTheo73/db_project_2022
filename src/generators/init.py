import sqlite3, json, os
from data_generator import generate as generate_data
from globals import *

def insert_person(person, db):
    db.execute("INSERT INTO people VALUES (?, ?, ?, ?, ?, ?)", [
            person["id"], person["name"], person["surname"], 
            person["birthdate"], person["phone"], person["nationality"]])

def insert_player(footballer, db):
    db.execute("INSERT INTO player VALUES (?, ?, ?, ?)", [
            footballer["athlete_id"], footballer["id"],
            footballer["team_name"], footballer["position"]])

def insert_referee(referee, db):
    db.execute("INSERT INTO referee VALUES (?, ?, ?)", [
            referee["referee_id"], referee["id"],
            referee["type"]])

def insert_team(team, db):
    db.execute("INSERT INTO team VALUES (?, ?, ?)", [
            team["team_name"], 
            team["stadium"],
            team["foundation_year"]])

def insert_match(match, db):
    db.execute("INSERT INTO match VALUES (?, ?, ?, ?)", [
            match["match_id"],
            match["datime"],
            match["home_team_goals"],
            match["away_team_goals"]])

def insert_participation(participation, db):
    db.execute("INSERT INTO participation VALUES (?, ?, ?)", [
            participation["match"],
            participation["home_team"],
            participation["away_team"]])

def insert_control(control, db):
    db.execute("INSERT INTO control VALUES (?, ?)", [
            control["match_id"],
            control["referee_id"]])

def insert_data(db):
    persons_stream = open(PEOPLE_PATH, "r")
    persons = json.load(persons_stream)
    persons_stream.close()
    for person in persons:
        insert_person(person, db)

    teams_stream = open(TEAMS_PATH, "r")
    teams = json.load(teams_stream)
    teams_stream.close()
    for team in teams:
        insert_team(team, db)

    footballers_stream = open(FOOTBALLERS_PATH, "r")
    footballers = json.load(footballers_stream)
    footballers_stream.close()
    for footballer in footballers:
        insert_player(footballer, db)
    
    referees_stream = open(REFEREES_PATH, "r")
    referees = json.load(referees_stream)
    referees_stream.close()
    for referee in referees:
        insert_referee(referee, db)

    matches_stream = open(MATCHES_PATH, "r")
    matches = json.load(matches_stream)
    matches_stream.close()
    for match in matches:
        insert_match(match, db)

    participations_stream = open(PARTICIPATIONS_PATH, "r")
    participations = json.load(participations_stream)
    participations_stream.close()
    for participation in participations:
        insert_participation(participation, db)

    controls_stream = open(CONTROLS_PATH, "r")
    controls = json.load(controls_stream)
    controls_stream.close()
    for control in controls:
        insert_control(control, db)


def create_db():
    if os.path.exists(DB_PATH): os.remove(DB_PATH)

    db = sqlite3.connect(DB_PATH)

    db.execute("DROP TABLE IF EXISTS people")
    db.execute("DROP TABLE IF EXISTS team")
    db.execute("DROP TABLE IF EXISTS match")
    db.execute("DROP TABLE IF EXISTS participation")
    db.execute("DROP TABLE IF EXISTS footballer")
    db.execute("DROP TABLE IF EXISTS referee")
    db.execute("DROP TABLE IF EXISTS control")
    db.execute("DROP TABLE IF EXISTS statistic")

    db.execute("PRAGMA foreign_keys = ON")

    db.execute("CREATE TABLE IF NOT EXISTS people(\
    	people_id CHAR(10) NOT NULL PRIMARY KEY,\
    	name TEXT NOT NULL,\
        surname TEXT NOT NULL,\
        birthdate DATE,\
        tel TEXT,\
        nationality TEXT\
    )")

    db.execute("CREATE TABLE IF NOT EXISTS team(\
    	team_name TEXT NOT NULL PRIMARY KEY,\
    	home TEXT,\
        founded DATE\
    )")

    db.execute("CREATE TABLE IF NOT EXISTS match(\
    	match_id INTEGER NOT NULL PRIMARY KEY,\
        datime DATETIME,\
        home_team_goals INTEGER,\
        away_team_goals INTEGER\
    )")

    db.execute("CREATE TABLE IF NOT EXISTS participation(\
        match_id INTEGER NOT NULL,\
        home_team TEXT NOT NULL,\
        away_team TEXT NOT NULL,\
        PRIMARY KEY (match_id),\
        FOREIGN KEY (match_id) REFERENCES match(match_id),\
        FOREIGN KEY (home_team) REFERENCES team(team_name),\
        FOREIGN KEY (away_team) REFERENCES team(team_name)\
    )")

    db.execute("CREATE TABLE IF NOT EXISTS player(\
        player_id CHAR(10) NOT NULL PRIMARY KEY,\
        people_id CHAR(10) NOT NULL,\
        team_name TEXT,\
        position VARCHAR(3),\
        FOREIGN KEY(people_id) REFERENCES people(people_id),\
        FOREIGN KEY(team_name) REFERENCES team(team_name)\
    )")

    db.execute("CREATE TABLE IF NOT EXISTS referee(\
        referee_id CHAR(10) NOT NULL PRIMARY KEY,\
        people_id CHAR(10) NOT NULL,\
        type TEXT,\
        FOREIGN KEY(people_id) REFERENCES people(people_id)\
    )")

    db.execute("CREATE TABLE IF NOT EXISTS control(\
        match_id INTEGER NOT NULL,\
        referee_id CHAR(10) NOT NULL,\
        FOREIGN KEY(match_id) REFERENCES match(match_id)\
        FOREIGN KEY(referee_id) REFERENCES referee(referee_id)\
    )")

    db.execute("CREATE TABLE IF NOT EXISTS statistic(\
        statistic_id INTEGER NOT NULL PRIMARY KEY,\
        match_id INTEGER NOT NULL,\
        player_id CHAR(10),\
        minute INTEGER,\
        stat_name TEXT,\
        FOREIGN KEY(match_id) REFERENCES match(match_id),\
        FOREIGN KEY(player_id) REFERENCES player(player_id)\
    )")

    return db


if __name__ == "__main__":
    generate_data(200, 50, 10)
    db = create_db()
    insert_data(db)
    db.commit()
    db.close()
