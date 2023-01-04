import json
from generators.random_generator import random_date, random_time
from numpy import random as nrandom
from generators.globals import *

def participations_generator(teams, matches):
    match_index = 0
    participations = []
    for i in range(0, len(teams), 1):
        home_team = teams[i]["team_name"]
        for j in range(0, len(teams), 1):
            away_team = teams[j]["team_name"]
            if (home_team != away_team):
                participations.append (
                    {
                        "match"     : matches[match_index]["match_id"],
                        "home_team" : home_team,
                        "away_team" : away_team
                    }
                )
                match_index += 1
                #print(home_team, away_team, match_index, sep="    ")
    return participations

def match_generator(match_id, season):
    prob = [0.15, 0.15, 0.2, 0.15, 0.15, 0.1, 0.05, 0.05]
    goals = [0, 1, 2, 3, 4, 5, 6, 7]
    home_team_goals = int(nrandom.choice(goals, p = prob, size=(1))[0])
    away_team_goals = int(nrandom.choice(goals, p = prob, size=(1))[0])
    date = random_date(start_year=season, end_year=season+1)
    time = random_time()
    return {
        "match_id"        : match_id,
        "datime"          : date+" "+time,
        "home_team_goals" : home_team_goals,
        "away_team_goals" : away_team_goals
    }


def generate(teams, season):
    no_of_teams = len(teams)
    no_of_matches = (no_of_teams) * (no_of_teams - 1)
    matches_stream = open(MATCHES_PATH, "w")
    participations_stream = open(PARTICIPATIONS_PATH, "w")
    print("Generating matches...")
    matches_stream.write("[\n")
    for i in range(no_of_matches):
        mymatch = match_generator(i, season)
        matches_stream.write(json.dumps(mymatch))
        if (i < no_of_matches - 1): 
            matches_stream.write(",\n")
        else:
            matches_stream.write("\n]")
    matches_stream.close()
    
    matches_stream = open(MATCHES_PATH, "r")
    matches = json.load(matches_stream)
    matches_stream.close()
    
    print("Generating participations...")
    participations = participations_generator(teams, matches)
    participations_stream.write("[\n")
    for i in range(0, len(participations), 1):
        participation = participations[i]
        participations_stream.write(json.dumps(participation))
        if (i < len(participations) - 1):
            participations_stream.write(",\n")
        else:
            participations_stream.write("\n]")
    participations_stream.close()

if __name__ == "__main__":
    teams_stream = open(TEAMS_PATH, "r")
    teams = json.load(teams_stream)
    teams_stream.close()
    generate(teams)