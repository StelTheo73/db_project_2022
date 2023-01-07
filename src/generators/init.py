import sqlite3, json, os
from generators.data_generator import generate as generate_data
from generators.statistics_generator import generate as generate_statistics
from generators.globals import *


def insert_person(person, db:sqlite3.Connection):
    db.execute("INSERT INTO people VALUES (?, ?, ?, ?, ?, ?)", [
        person["id"], person["name"], person["surname"], 
        person["birthdate"], person["phone"], person["nationality"]])

def insert_player(footballer, db:sqlite3.Connection):
    db.execute("INSERT INTO player VALUES (?, ?, ?, ?)", [
        footballer["athlete_id"], footballer["id"],
        footballer["team_name"], footballer["position"]])

def insert_referee(referee, db:sqlite3.Connection):
    db.execute("INSERT INTO referee VALUES (?, ?, ?)", [
        referee["referee_id"], referee["id"],
        referee["type"]])

def insert_team(team, db:sqlite3.Connection):
    db.execute("INSERT INTO team VALUES (?, ?, ?)", [
        team["team_name"], team["stadium"],
        team["foundation_year"]])

def insert_match(match, db:sqlite3.Connection):
    db.execute("INSERT INTO match VALUES (?, ?, ?, ?)", [
        match["match_id"],
        match["datime"],
        match["home_team_goals"],
        match["away_team_goals"]])

def insert_participation(participation, db:sqlite3.Connection):
    db.execute("INSERT INTO participation VALUES (?, ?, ?)", [
        participation["match"],
        participation["home_team"], participation["away_team"]])

def insert_control(control, db:sqlite3.Connection):
    db.execute("INSERT INTO control VALUES (?, ?)", [
        control["match_id"], control["referee_id"]])

def insert_statistic(statistic, db:sqlite3.Connection):
    db.execute("INSERT INTO statistic VALUES (?, ?, ?, ?, ?)", [
        statistic["statistic_id"], statistic["match_id"],
        statistic["player_id"],
        statistic["minute"], statistic["stat_name"]])

data_path_map = {
    PEOPLE_PATH : insert_person,
    TEAMS_PATH  : insert_team,
    FOOTBALLERS_PATH : insert_player,
    REFEREES_PATH : insert_referee,
    MATCHES_PATH : insert_match,
    PARTICIPATIONS_PATH : insert_participation,
    CONTROLS_PATH : insert_control,
}

def insert_data():
    get_data(data_path_map)

def insert_statistics():
    get_data({STATISTICS_PATH: insert_statistic})

def get_data(path_map):
    for path in path_map:
        try:
            with open(path, "r") as stream:
                content = json.load(stream)
            os.remove(path) # delete json file
            for item in content:
                path_map[path](item, db)
        except FileNotFoundError:
            print(f"Could not find {path}")

def initialize(players, referees, teams, season):
    global db
    db = sqlite3.connect(DB_PATH)
    flush()
    # insert data (not statistics)
    generate_data(players, referees, teams, season)
    insert_data()
    # insert statistics (need to have inserted all previous data first)
    generate_statistics()
    insert_statistics()
    # Commit changes and clode database
    db.commit()
    db.close()
    print("Initialization completed!")

def flush():
    # Execute the external SQL script
    with open(SQL_PATH, 'r') as sql_file:
        db.executescript(sql_file.read())
    db.commit()
    print("Flush completed!")

if __name__ == "__main__":
    initialize()