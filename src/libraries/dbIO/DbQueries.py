import sqlite3
from generators import random_generator

class DbQueries:

    ## Static Variables
    DB_PATH = './src/data/database.db'
    db = sqlite3.connect(DB_PATH)

    @staticmethod
    def submit(entries={}, method=None):        ## Needs a looot of Error Handling
        inputs = {func: entries[func].get() for func in entries}

        if method != DbQueries.run_query:
            for func in entries:    # Clear entries
                try: entries[func].set('')  # for ComboBox
                except AttributeError: entries[func].delete(0,'end')   # for Entry

        # print(inputs)
        if method != None: method(inputs)
        
    @staticmethod
    def update_players(inputs):
        print("Submited player!")

        DbQueries.update_persons(inputs)

        DbQueries.db.execute("INSERT INTO player (player_id, person_id, club, position) VALUES (?,?,?,?)",
            [inputs['card'], inputs['id'], inputs['club'], inputs['position']])
        DbQueries.db.commit()
    
    @staticmethod
    def update_referees(inputs):
        print("Submited referee!")

        DbQueries.update_persons(inputs)

        DbQueries.db.execute("INSERT INTO referee (referee_id, person_id, position) VALUES (?,?,?)",
            [inputs['card'], inputs['id'], inputs['position']])
        DbQueries.db.commit()
    
    @staticmethod
    def update_persons(inputs):
        print("Submited person!")

        date = '-'.join([inputs['year'], inputs['month'], inputs['day']])
        DbQueries.db.execute("INSERT INTO people (id, name, surname, birthdate, tel, nationality) VALUES (?,?,?, DATE(?), ?,?)",
            [inputs['id'], inputs['name'], inputs['surname'], date, inputs['tel'], inputs['nationality']])
        DbQueries.db.commit()
    
    @staticmethod
    def update_clubs(inputs):
        print("Submited team!")

        date = inputs['founded'] + '-01-01'
        DbQueries.db.execute("INSERT INTO team (team_name, home, founded) VALUES (?,?, DATE(?))", [inputs['name'], inputs['home'], date])
        DbQueries.db.commit()

    @staticmethod
    def update_matches(inputs):
        print("Submited match!")

        datetime = '-'.join([inputs[i] for i in ['year','month','day']]) +' '+ inputs['hour']+':'+inputs['minute']

        DbQueries.db.execute("INSERT INTO match (datime, home_goals, away_goals) VALUES (DATETIME(?),?,?)",
            [datetime, inputs['home_score'], inputs['away_score']])
        
        match_id = DbQueries.db.execute("SELECT id FROM matches").fetchall()[-1][0]

        DbQueries.db.execute("INSERT INTO participation (match_id, home_team, away_team) VALUES (?,?,?)",
            [match_id, inputs['home_team'], inputs['away_team']])
        
        DbQueries.db.execute("INSERT INTO control (match_id, referee_id) VALUES (?,?)",
            [match_id, inputs['head_ref']])

        DbQueries.db.execute("INSERT INTO control (match_id, referee_id) VALUES (?,?)",
            [match_id, inputs['assist_ref_1']])

        DbQueries.db.execute("INSERT INTO control (match_id, referee_id) VALUES (?,?)",
            [match_id, inputs['assist_ref_2']])

        DbQueries.db.execute("INSERT INTO control (match_id, referee_id) VALUES (?,?)",
            [match_id, inputs['fourth_ref']])

        DbQueries.db.commit()

    @staticmethod
    def update_stats(inputs):
        print("Submited statistic!")
        #TODO


    @staticmethod
    def run_query(inputs):
        print("Submited Query!")
        query = inputs['query']

        try:
            data = DbQueries.db.execute(query).fetchall()
            print(*data, sep='\n')
        except Exception as e:
            print(e)
