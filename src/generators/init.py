import sqlite3, json, os
from generators.data_generator import generate as generate_data
from generators.statistics_generator import generate as generate_statistics
from generators.globals import *

db = sqlite3.connect(DB_PATH)

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
            control["referee_id"]
        ])

def insert_statistic(statistic, db):
    db.execute("INSERT INTO statistic VALUES (?, ?, ?, ?, ?)", [
        statistic["statistic_id"],
        statistic["match_id"],
        statistic["player_id"],
        statistic["minute"],
        statistic["stat_name"]
    ])

path_map = {
    PEOPLE_PATH : insert_person,
    TEAMS_PATH  : insert_team,
    FOOTBALLERS_PATH : insert_player,
    REFEREES_PATH : insert_referee,
    MATCHES_PATH : insert_match,
    PARTICIPATIONS_PATH : insert_participation,
    CONTROLS_PATH : insert_control,
}

def insert_data(db):
    for path in path_map.keys():
        try:
            stream = open(path, "r")
            content = json.load(stream)
            stream.close()
            for item in content:
                path_map[path](item, db)
            db.commit()
        except FileNotFoundError:
            print("Could not find {}".format(path))
            continue

def clear_data():
    for path in path_map.keys():
        os.remove(path)
    os.remove(STATISTICS_PATH)

def insert_statistics(db):
    try:
        stream = open(STATISTICS_PATH, "r")
        content = json.load(stream)
        stream.close()
        for item in content:
            insert_statistic(item, db)
        db.commit()
    except FileNotFoundError:
        print("Could not find {}".format(STATISTICS_PATH)) 

def create_db():
    #if os.path.exists(DB_PATH): os.remove(DB_PATH)
    db = sqlite3.connect(DB_PATH)
    flush()
    
    db.execute("PRAGMA foreign_keys = ON")

    db.execute("CREATE TABLE IF NOT EXISTS people(\
    	people_id CHAR(8) NOT NULL PRIMARY KEY,\
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
        people_id CHAR(8) NOT NULL,\
        team_name TEXT,\
        position VARCHAR(3),\
        FOREIGN KEY(people_id) REFERENCES people(people_id),\
        FOREIGN KEY(team_name) REFERENCES team(team_name)\
    )")

    db.execute("CREATE TABLE IF NOT EXISTS referee(\
        referee_id CHAR(10) NOT NULL PRIMARY KEY,\
        people_id CHAR(8) NOT NULL,\
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

def initialize(players, referees, teams, season):
    generate_data(players, referees, teams, season)
    db = create_db()
    insert_data(db)
    generate_statistics()
    insert_statistics(db)
    db.commit()
    db.close()
    print("Initialization completed!")
    clear_data()

def flush():
    db = sqlite3.connect(DB_PATH)
    db.execute("DROP TABLE IF EXISTS people")
    db.execute("DROP TABLE IF EXISTS team")
    db.execute("DROP TABLE IF EXISTS match")
    db.execute("DROP TABLE IF EXISTS participation")
    db.execute("DROP TABLE IF EXISTS player")
    db.execute("DROP TABLE IF EXISTS referee")
    db.execute("DROP TABLE IF EXISTS control")
    db.execute("DROP TABLE IF EXISTS statistic")
    db.close()
    print("Flush completed!")

if __name__ == "__main__":
    initialize()