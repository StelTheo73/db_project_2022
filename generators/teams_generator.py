import random
import random_generator as rndg
import json

teams = []

teams_name_list = []

def team_generator():
    name = random.choice(rndg.lorem_ipsum).capitalize() + " " + random.choice(rndg.lorem_ipsum).capitalize()
    while(name in teams_name_list or name.split(" ")[0] == "" or name.split(" ")[1] == "" or name == " "):
            name = random.choice(rndg.lorem_ipsum).capitalize() + " " + random.choice(rndg.lorem_ipsum).capitalize()
    teams_name_list.append(name)            
    foundation = random.randint(1900, 2022)
    stadium = random.choice(rndg.lorem_ipsum).capitalize() + " " + random.choice(rndg.lorem_ipsum).capitalize()
    while(stadium.split(" ")[0] == "" or stadium.split(" ")[1] == "" or stadium == " "):
        stadium = random.choice(rndg.lorem_ipsum).capitalize() + " " + random.choice(rndg.lorem_ipsum).capitalize()
    return {
        "team_name" : name,
        "foundation_year" : foundation,
        "stadium" : stadium 
    }

def generate(no_of_teams = 16):
    teams_stream = open("./json_files/teams.json", "w")
    print("Generating teams...")
    teams_stream.write("[\n")
    for i in range(no_of_teams):
        team = team_generator()
        teams.append(team)
        teams_stream.write(json.dumps(team))
        if (i < no_of_teams - 1):
            teams_stream.write(",\n")
    teams_stream.write("\n]")
    teams_stream.close()

if __name__ == "__main__":
    generate(200)