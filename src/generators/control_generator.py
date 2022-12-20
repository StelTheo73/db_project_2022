import json, random
from globals import *

def control_generator(ref_type, referees, match_id):
    type = None
    while(type != ref_type):
        ref = random.choice(referees)
        type = ref["type"]
    return {
                "match_id"    : match_id,
                "referee_id"  : ref["referee_id"]
            }

def generate(matches, referees):
    print("Linking refs with matches...")
    control_stream = open(CONTROLS_PATH, "w")
    control_stream.write("[\n")
    for i in range(0, len(matches), 1):
        head = control_generator("Head", referees, matches[i]["match_id"])        
        control_stream.write(json.dumps(head))
        control_stream.write(",\n")
        
        assistant1 = control_generator("Assistant", referees, matches[i]["match_id"])
        control_stream.write(json.dumps(assistant1))
        control_stream.write(",\n")
        
        assistant2 = control_generator("Assistant", referees, matches[i]["match_id"])
        while(assistant1 == assistant2):
            assistant2 = control_generator("Assistant", referees, matches[i]["match_id"])
        control_stream.write(json.dumps(assistant2))
        control_stream.write(",\n")

        fourth = control_generator("Fourth", referees, matches[i]["match_id"])
        control_stream.write(json.dumps(fourth))
        if (i < len(matches) - 1):
            control_stream.write(",\n")
        else:
            control_stream.write("\n]")
    control_stream.close()
        
if __name__ == "__main__":
    matches_stream = open(MATCHES_PATH, "r")
    referees_stream = open(REFEREES_PATH, "r")
    matches = json.load(matches_stream)
    referees = json.load(referees_stream)
    matches_stream.close()
    referees_stream.close()
    generate(matches, referees)