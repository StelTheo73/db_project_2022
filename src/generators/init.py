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
    # EXECUTE THE EXTERNAL SQL SCRIPT
    with open(SQL_PATH, 'r') as sql_file:
        db.executescript(sql_file.read())
    db.commit()
    # db.close()


def initialize(players, referees, teams, season):
    flush()
    # create_db()
    generate_data(players, referees, teams, season)
    insert_data(db)
    generate_statistics()
    insert_statistics(db)
    db.commit()
    db.close()
    print("Initialization completed!")
    clear_data()

def flush():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    create_db()
    print("Flush completed!")

if __name__ == "__main__":
    initialize()