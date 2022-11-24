import sqlite3

class QuerySelector():  # Maybe make it two different classes?

    ## Static Variables
    DB_PATH = './src/db/database.db'
    db = sqlite3.connect(DB_PATH)   # These have to be kinda global for all files (or not)


    @staticmethod
    def submit(entries={}, method=None): # Needs a looot of Error Handling
        inputs = {}
        for func in entries:
            entries[func].get()
            input = entries[func].get()
            try: entries[func].set('')  # for ComboBox
            except AttributeError: entries[func].delete(0,'end')   # for Entry
            
            inputs[func] = input

        print(inputs)
        if method != None: method(inputs)
        

    @staticmethod
    def update_players(inputs):
        print("Submited player!")

        QuerySelector.update_persons(inputs)

        QuerySelector.db.execute("INSERT INTO players VALUES (?,?,?,?)",
            [inputs['card'], inputs['id'], inputs['club'], inputs['position']])
        QuerySelector.db.commit()
    
    @staticmethod
    def update_referees(inputs):
        print("Submited referee!")

        QuerySelector.update_persons(inputs)

        QuerySelector.db.execute("INSERT INTO referees VALUES (?,?,?)",
            [inputs['card'], inputs['id'], inputs['position']])
        QuerySelector.db.commit()
    
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

        datetime = '-'.join([inputs[i] for i in ['year','month','day']]) +' '+ inputs['hour']+':'+inputs['minute']
        x = QuerySelector.db.execute("INSERT INTO matches (datime, home_goals, away_goals) VALUES (DATETIME(?),?,?)",
            [datetime, inputs['home_score'], inputs['away_score']])
        
        match_id = QuerySelector.db.execute("SELECT id FROM matches").fetchall()[-1][0]

        QuerySelector.db.execute("INSERT INTO participations (home_team, away_team) VALUES (?,?)",
            [inputs['home_team'], inputs['away_team']])
        
        QuerySelector.db.execute("INSERT INTO controls VALUES (?,?)",
            [match_id, inputs['referee']])

        QuerySelector.db.commit()

    @staticmethod
    def update_stats(inputs):
        print("Submited statistic!")


    ## ------------------------------------------------------------------------------------------------------------

    
    @staticmethod
    def getTeams():
        return [club[0] for club in QuerySelector.db.execute("SELECT name FROM clubs")]

    @staticmethod
    def getPositions():
        # return ["Attacker", "Midfielder", "Defender", "Goalkeeper"]
        return [
            "ST", "CF", "LW", "RW",
            "LM", "CM", "CAM", "CDM", "RM",
            "LWB", "LB", "CB", "RB", "RWB",
            "GK"]
    
    @staticmethod
    def getRefPositions():
        return ["headref#0", "assistref#1", "assistref#2", "fourthref#4"]
    
    @staticmethod
    def getReferees():
        return [ref[0] for ref in QuerySelector.db.execute("SELECT * FROM referees")]

