import random
import random_generator as rndg
import json

domains = ["gmail", "hotmail", "yahoo"]

positions = ["ATT", "MID", "DEF", "GK"]

ref_types = ["Head", "Assistant", "Fourth"]

persons_id_list = []
footballers_id_list = []
referees_id_list = []

names = json.load(open("./src/libraries/JsonFiles/names.json"))
firstnames = names["firstnames"]
lastnames = names["lastnames"]

def person_generator():
    id = rndg.random_choice(rndg.upper_letters, 2) + rndg.random_choice(rndg.numbers, 6)
    while(id in persons_id_list):
        id = rndg.random_choice(rndg.upper_letters, 2) + rndg.random_choice(rndg.numbers, 6)
    persons_id_list.append(id)
    name = random.choice(firstnames)
    last_name = random.choice(lastnames)
    birthday = rndg.random_date()
    phone = "69" + rndg.random_choice(rndg.numbers, 8)
    address = random.choice(rndg.lorem_ipsum).capitalize() + " " + random.choice(rndg.lorem_ipsum).capitalize() + " " + str(random.randint(1, 99)) + ", " + random.choice(rndg.lorem_ipsum).capitalize() + ", " + random.choice(rndg.countries)[1]
    nationality = random.choice(rndg.countries)[1]
    email = name + rndg.random_email()
    return {
        "name"        : name,
        "surname"     : last_name,
        "id"          : id,
        "birthdate"   : birthday,
        "phone"       : phone,
        "email"       : email,
        "address"     : address,
        "nationality" : nationality
    }

def footballer_generator(person_id, team_name):
    card_id = rndg.random_choice(rndg.upper_letters+rndg.numbers, 10) 
    while(card_id in footballers_id_list):
        card_id = rndg.random_choice(rndg.upper_letters+rndg.numbers, 10) 
    footballers_id_list.append(card_id)    
    position = random.choice(positions)
    return {
        "id"         : person_id, 
        "athlete_id" : card_id, 
        "position"   : position, 
        "team_name"  : team_name
    }

def referee_generator(person_id):
    card_id = rndg.random_choice(rndg.upper_letters+rndg.numbers, 10)
    while(card_id in footballers_id_list):
        card_id = rndg.random_choice(rndg.upper_letters+rndg.numbers, 10) 
    referees_id_list.append(card_id)        
    type = random.choice(ref_types)
    return {
        "id"         : person_id,
        "referee_id" : card_id, 
        "type"       : type
    }
    
def generate(teams, no_of_footballers = 300, no_of_refs = 50):
    persons_stream = open("./json_files/persons.json", "w")
    footballers_stream = open("./json_files/footballers.json", "w")
    referees_stream = open("./json_files/referees.json", "w")

    print("Generating footballers...")
    persons_stream.write("[\n")
    footballers_stream.write("[\n")
    for i in range(no_of_footballers):
        person = person_generator()
        footballer = footballer_generator(person["id"], random.choice(teams)["team_name"])
        persons_stream.write(json.dumps(person))
        footballers_stream.write(json.dumps(footballer))
        persons_stream.write(",\n")
        if (i < no_of_footballers - 1):
            footballers_stream.write(",\n")
        else:
            footballers_stream.write("\n]")

    print("Generating refs...")
    referees_stream.write("[\n")
    for i in range(no_of_refs):
        person = person_generator()
        referee = referee_generator(person["id"])
        persons_stream.write(json.dumps(person))
        referees_stream.write(json.dumps(referee))
        if(i < no_of_refs - 1):
            referees_stream.write(",\n")
            persons_stream.write(",\n")
        else:
            referees_stream.write("\n]")
            persons_stream.write("\n]")

    persons_stream.close()

if __name__ == "__main__":
    teams_stream = open("./json_files/teams.json", "r")
    teams = json.load(teams_stream)
    teams_stream.close()
    generate(teams, 300, 50)