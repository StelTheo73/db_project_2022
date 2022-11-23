from tkcalendar import Calendar
import sqlite3

class QuerySelector():  # Maybe make it two different classes?

    # Static Variables
    DB_PATH = './src/db/database.db'
    db = sqlite3.connect(DB_PATH)   # These have to be kinda global for all files (or not)


    @staticmethod
    def submit(entries={}, method=None): # Needs a looot of Error Handling
        inputs = {}
        for func in entries:
            if entries[func].__class__ == Calendar:
                input = entries[func].get_date()
                input = "19"+"-".join(reversed(input.split("/"))) # FUCK MEEE .!.
            else:
                entries[func].get()
                input = entries[func].get()
                entries[func].delete(0,'end')
            
            inputs[func] = input

        # print(inputs)
        if method != None: method(inputs)
            

    @staticmethod
    def update_players(inputs):
        print("Submited player!")

        QuerySelector.db.execute("INSERT INTO players VALUES (?,?,?,?)",
            [inputs['card'], inputs['id'], inputs['club'], inputs['position']])
        QuerySelector.db.commit()

        QuerySelector.update_persons(inputs)
    
    @staticmethod
    def update_referees(inputs):
        print("Submited referee!")

        ## IMPLEMENT GUI REFEREE POSITIONS
        # QuerySelector.db.execute("INSERT INTO referees VALUES (?,?,?,?)",
        #     [inputs['card'], inputs['id'], inputs['position']])
        # QuerySelector.db.commit()

        QuerySelector.update_persons(inputs)
    
    @staticmethod
    def update_persons(inputs):
        print("Submited person!")

        date = '-'.join([inputs['year'], inputs['month'], inputs['day']])
        QuerySelector.db.execute("INSERT INTO people VALUES (?,?,?, DATE(?), ?,?)",
            [inputs['id'], inputs['name'], inputs['surname'], date, inputs['tel'], inputs['nationality']])
        QuerySelector.db.commit()
    
    @staticmethod
    def update_clubs(inputs):
        print("Submited club!")

        date = inputs['founded'] + '-01-01'
        QuerySelector.db.execute("INSERT INTO clubs VALUES (?,?, DATE(?))", [inputs['name'], inputs['home'], date])
        QuerySelector.db.commit()

    @staticmethod
    def update_matches(inputs):
        print("Submited match!")

        ## IMPLEMENT GUI MATCHES
        # date = '-'.join([inputs['year'], inputs['month'], inputs['day']])
        # QuerySelector.db.execute("INSERT INTO matches VALUES (?,?,?,?)",
        #     [inputs['id'], date, inputs['home_score'], inputs['away_score']])
        # QuerySelector.db.commit()


    ## ------------------------------------------------------------------------------------------------------------

    
    @staticmethod
    def getTeams():
        return [club[0] for club in QuerySelector.db.execute("SELECT name FROM clubs")]
        # ["Team1", "Team2", "Team3", "Team4", "Team5", "Team6", "Team7", "Team8", "Team9", "Team10"]

    @staticmethod
    def getPositions():
        return ["Attacker", "Midfielder", "Defender", "Goalkeeper"]

    @staticmethod
    def getSpecificPositions():
        return [
            "ST", "CF", "LW", "RW", 
            "LM", "CM", "CAM", "CDM", "RM",
            "LWB", "LB", "CB", "RB", "RWB",
            "GK"]

