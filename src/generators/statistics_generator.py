import sqlite3
import random
import json
import os
from globals import *
from numpy import random as nrandom

db = sqlite3.connect(DB_PATH)

empty_player = {
    "player_id" : None,
    "position"   : None
}

def get_matches():
    matches_list = []
    [matches_list.append(match) for match in db.execute("SELECT match.match_id, home_team, away_team, home_team_goals, away_team_goals \
                FROM match, participation \
                WHERE match.match_id = participation.match_id")
    ]
    matches_list_dict = []
    for match in matches_list:
        match_dict = {
            "match_id"        : match[0],
            "home_team"       : match[1],
            "away_team"       : match[2],
            "home_team_goals" : match[3],
            "away_team_goals" : match[4],
        }
        matches_list_dict.append(match_dict)

    return matches_list_dict

def get_players(team):
    players_list = []
    [players_list.append(player) for player in db.execute("SELECT player_id, position \
                FROM player, team \
                WHERE player.team_name = ?", [team])
    ]
    players_list_dict = []
    for player in players_list:
        player_dict = {
            "player_id" : player[0],
            "position"  : player[1]
        }
        players_list_dict.append(player_dict)
    return players_list_dict

def select_random_players_by_position(players, position, number):
    selected_players = []
    player = empty_player
    for _ in range(number):
        while(player["position"] != position):
            player = random.choice(players)
        selected_players.append(player)
    return selected_players

def simulate_match(match, stat_id):
    statistics_list = []
    home_team_players = get_players(match["home_team"])
    away_team_players = get_players(match["away_team"])
    minutes = [m for m in range(0, 91)]
    #print(home_team_players)
    #print(away_team_players)
    #home_team_on_players = select_random_players_by_position(home_team_players, "GK", 1) + \
    #                        select_random_players_by_position(home_team_players, "DEF", 4) + \
    #                        select_random_players_by_position(home_team_players, "MID", 3) + \
    #                        select_random_players_by_position(home_team_players, "ATT", 3)
    
    #away_team_on_players = select_random_players_by_position(away_team_players, "GK", 1) + \
    #                        select_random_players_by_position(away_team_players, "DEF", 4) + \
    #                        select_random_players_by_position(away_team_players, "MID", 3) + \
    #                        select_random_players_by_position(away_team_players, "ATT", 3)
    home_team_on_players = home_team_players
    away_team_on_players = away_team_players
    #print("selected_eleven")

    # Penalties & Fouls
    #print("penalties & fouls")
    red_players = []
    yellow_players = []
    penalties = nrandom.choice([0, 1, 2], p = [0.88, 0.1, 0.02], size=(1))[0]
    fouls = nrandom.choice([0, 1, 2, 3, 4, 5, 6, 7], p = [0.05, 0.1, 0.15, 0.2, 0.2, 0.15, 0.1, 0.05], size=(1))[0]
    for i in range(1, penalties+fouls+1, 1):
        commited_team_player = nrandom.choice(["H", "A"], p=[0.5, 0.5], size=(1))[0]
        if commited_team_player == "H":
            commited_player = random.choice(home_team_on_players)
            kick_player = random.choice(away_team_on_players)
            while (kick_player["position"] == "GK"):
                kick_player = random.choice(away_team_on_players)
        else:
            commited_player = random.choice(away_team_on_players)
            kick_player = random.choice(home_team_on_players)
            while (kick_player["position"] == "GK"):
                kick_player = random.choice(home_team_on_players)
        minute = random.choice(minutes)

        # Give Card on Foul/Penalty
        card = nrandom.choice(["No", "Yellow", "Red"], p = [0.49, 0.49, 0.02], size = (1))[0]
        if card != "No":
            if card == "Red": # Red Card -> expelled
                red_players.append(commited_player)
                if commited_player == "H":
                    home_team_on_players.remove(commited_player)
                elif commited_player == "A":
                    away_team_on_players.remove(commited_player)
                statistics_list.append(generate_statistic("Red Card", minute, match["match_id"], commited_player["player_id"], stat_id))
                stat_id +=1
            elif card == "Yellow": # Yellow Card
                if commited_player not in yellow_players: # First Yellow Card
                    yellow_players.append(commited_player)
                else:
                    yellow_players.remove(commited_player) # Second Yellow Card -> expelled
                    if commited_player == "H":
                        home_team_on_players.remove(commited_player)
                    elif commited_player == "A":
                        away_team_on_players.remove(commited_player)
                    red_players.append(commited_player)
                statistics_list.append(generate_statistic("Yellow Card", minute, match["match_id"], commited_player["player_id"], stat_id))
                stat_id+=1

        if i <= penalties:
            statistics_list.append(generate_statistic("Penalty Commited", minute, match["match_id"], commited_player["player_id"], stat_id))
            stat_id+=1
            statistics_list.append(generate_statistic("Penalty Kick", minute, match["match_id"], kick_player["player_id"], stat_id))
            stat_id+=1
        else:
            statistics_list.append(generate_statistic("Foul Commited", minute, match["match_id"], commited_player["player_id"], stat_id))
            stat_id+=1
            statistics_list.append(generate_statistic("Foul Kick", minute, match["match_id"], kick_player["player_id"], stat_id))
            stat_id+=1

    # Home Team Goals & Assists
    goals = match["home_team_goals"]
    #print("home goals")
    for _ in range(goals):
        minute = random.choice(minutes)
        is_own_goal = nrandom.choice([0, 1], p=[0.98, 0.02], size=(1))[0]
        if is_own_goal:
            player = random.choice(away_team_players)
            statistics_list.append(generate_statistic("Own Goal", minute, match["match_id"], player["player_id"], stat_id))
            stat_id+=1
        else:
            player = random.choice(home_team_on_players)
            while player["position"] == "GK":
                player = random.choice(home_team_on_players)
            statistics_list.append(generate_statistic("Goal", minute, match["match_id"], player["player_id"], stat_id))
            stat_id+=1
            assist_player = random.choice(home_team_on_players)
            while assist_player["player_id"] == player["player_id"]:
                assist_player = random.choice(home_team_on_players)
            statistics_list.append(generate_statistic("Assist", minute, match["match_id"], assist_player["player_id"], stat_id))
            stat_id+=1

    # Away Team Goals & Assists
    goals = match["away_team_goals"]
    #print("away goals")
    for _ in range(goals):
        minute = random.choice(minutes)
        is_own_goal = nrandom.choice([0, 1], p=[0.98, 0.02], size=(1))[0]
        if is_own_goal:
            player = random.choice(home_team_on_players)
            statistics_list.append(generate_statistic("Own Goal", minute, match["match_id"], player["player_id"], stat_id))
            stat_id+=1
        else:
            player = random.choice(away_team_on_players)
            while player["position"] == "GK":
                player = random.choice(away_team_on_players)
            statistics_list.append(generate_statistic("Goal", minute, match["match_id"], player["player_id"], stat_id))
            stat_id+=1
            assist_player = random.choice(away_team_on_players)
            while assist_player["player_id"] == player["player_id"]:
                assist_player = random.choice(away_team_on_players)
            statistics_list.append(generate_statistic("Assist", minute, match["match_id"], assist_player["player_id"], stat_id))
            stat_id+=1

    # Offsides and Corners
    #print("offsides & corners")
    offsides = nrandom.choice([0, 1, 2, 3, 4, 5], p = [0.05, 0.15, 0.3, 0.3, 0.15, 0.05], size=(1))[0]
    corners = nrandom.choice([0, 1, 2, 3, 4, 5, 6, 7], p = [0.05, 0.1, 0.15, 0.2, 0.2, 0.15, 0.1, 0.05], size=(1))[0]
    for i in range(1, offsides+corners+1, 1):
        team_player = nrandom.choice(["H", "A"], p=[0.5, 0.5], size=(1))[0]
        if team_player == "H":
            player = random.choice(home_team_on_players)
            while (player["position"] == "GK"):
                player = random.choice(home_team_on_players)
        else:
            player = random.choice(away_team_on_players)
            while (player["position"] == "GK"):
                player = random.choice(away_team_on_players)
        minute = random.choice(minutes)
        if i <= offsides:
            statistics_list.append(generate_statistic("Offside", minute, match["match_id"], player["player_id"], stat_id))
            stat_id+=1
        else:
            statistics_list.append(generate_statistic("Corner", minute, match["match_id"], player["player_id"], stat_id))
            stat_id+=1

    return statistics_list, stat_id


def generate_statistic(stat_name, minute, match_id, player_id, statistic_id):
    stat = {
        "statistic_id" : statistic_id,
        "match_id"     : match_id,
        "player_id"    : player_id,
        "minute"       : minute,
        "stat_name"    : stat_name
    }
    return stat

def generate():
    print("Simulating matches...")
    stat_id = 0
    matches = get_matches()
    statistics_stream = open(STATISTICS_PATH, "w")
    statistics_stream.write("[\n")
    for match in matches:
        stats_dict, stat_id = simulate_match(match, stat_id)
        for stat in stats_dict:
            statistics_stream.write(json.dumps(stat))
            statistics_stream.write(",\n")
    statistics_stream.close()

    # Remove last ","
    with open(STATISTICS_PATH, "rb+") as stream:
        stream.seek(-3, os.SEEK_END)
        stream.truncate()
    with open(STATISTICS_PATH, "a") as stream:
        stream.write("\n]")

if __name__ == "__main__":
    generate()