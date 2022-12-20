from persons_generator import generate as generate_persons
from teams_generator import generate as generate_teams
from matches_generator import generate as generate_matches
from control_generator import generate as generate_control
from globals import *
import json

def generate(num_of_footballers = 300, num_of_referees = 50, num_of_teams = 16):
    generate_teams(num_of_teams)
    teams_stream = open(TEAMS_PATH, "r")
    teams = json.load(teams_stream)
    teams_stream.close()
    generate_persons(teams, num_of_footballers, num_of_referees)
    generate_matches(teams)
    matches_stream = open(MATCHES_PATH, "r")
    matches = json.load(matches_stream)
    matches_stream.close()
    referees_stream = open(REFEREES_PATH, "r")
    referees = json.load(referees_stream)
    referees_stream.close()
    generate_control(matches, referees)

if __name__ == "__main__":
    generate(300, 50)