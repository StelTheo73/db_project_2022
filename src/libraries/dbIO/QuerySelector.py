import sqlite3, json

class QuerySelector():  # Maybe make it two or more different classes?

    ## Static Variables
    DB_PATH = './src/db/database.db'
    db = sqlite3.connect(DB_PATH)


    @staticmethod
    def submit(entries={}, method=None):        ## Needs a looot of Error Handling
        inputs = {func: entries[func].get() for func in entries}

        if method != QuerySelector.run_query:
            for func in entries:    # Clear entries
                try: entries[func].set('')  # for ComboBox
                except AttributeError: entries[func].delete(0,'end')   # for Entry

        # print(inputs)
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


    @staticmethod
    def run_query(inputs):
        print("Submited Query!")
        query = inputs['query']

        if query.split(' ')[0].upper() != 'SELECT':
            print("Please enter a SELECT Query..")

        try:
            data = QuerySelector.db.execute(query).fetchall()
            [print(d) for d in data]
        except Exception as e:
            print(e)


    ## ------------------------------------------------------------------------------------------------------------


    ## Static Variables
    JSON_PATH = './src/libraries/JsonFiles/'
    

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
    
    @staticmethod
    def getCountries():
        with open(QuerySelector.JSON_PATH+'countries.json') as f:
            countries = [d['name'] for d in json.loads(f.read())]
        return countries

