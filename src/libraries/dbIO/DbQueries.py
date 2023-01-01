import sqlite3, json, ctypes
from datetime import date

class QuerySelector:

    ## Static Variables
    JSONs_PATH = './src/libraries/JsonFiles/'
    
    @staticmethod
    def getMatches():
        try:
            return [f"{home}-{away} (match#{id})" for id,home,away in
                DbQueries.db.execute("SELECT match.match_id, home_team, away_team FROM match,participation WHERE match.match_id=participation.match_id")]
        except sqlite3.OperationalError:
            return []

    @staticmethod
    def getPeopleId(id):
        try:
            return [f"{people_id}" for people_id in
                DbQueries.db.execute("SELECT people_id FROM people WHERE people_id = ?",[id])]
        except sqlite3.OperationalError:
            return []

    @staticmethod
    def getPeopleIdFromPlayerId(player_id):
        try:
            return [f"{people_id}" for people_id in
                DbQueries.db.execute("SELECT people.people_id FROM people, player WHERE people.people_id = player.people_id AND player.player_id = ?",[player_id])]
        except sqlite3.OperationalError:
            return []

    @staticmethod
    def getPeopleIdFromRefereeId(referee_id):
        try:
            return [f"{people_id}" for people_id in
                DbQueries.db.execute("SELECT people.people_id FROM people, referee WHERE people.people_id = referee.people_id AND referee_id = ?",[referee_id])]
        except sqlite3.OperationalError:
            return []

    @staticmethod
    def getPlayers():
        try: 
            return [f"{lName} {fName} ({id})" for lName,fName,id in
                DbQueries.db.execute("SELECT surname, name, player_id FROM player,people WHERE player.people_id=people.people_id ORDER BY surname, name, player_id")]
        except sqlite3.OperationalError:
            return []

    @staticmethod
    def getPlayersByTeam(team):
        try:
            return [f"{lName} {fName} ({id})" for lName,fName,id in
                DbQueries.db.execute("SELECT surname, name, player_id FROM player,people WHERE player.people_id=people.people_id AND player.team_name=? ORDER BY surname, name, player_id",[team])]
        except sqlite3.OperationalError:
            return []

    @staticmethod
    def getReferees():
        try: 
            return [f"{lName} {fName} ({id})" for lName,fName,id in
                DbQueries.db.execute("SELECT surname, name, referee_id FROM referee,people  WHERE referee.people_id=people.people_id ORDER BY surname, name, referee_id")]
        except sqlite3.OperationalError:
            return []

    @staticmethod
    def getRefereesByType(type):
        try:
            return [f"{lName} {fName} ({id})" for lName,fName,id in
                DbQueries.db.execute("SELECT surname, name, referee_id FROM referee,people  WHERE referee.people_id=people.people_id AND referee.type=? ORDER BY surname, name, referee_id",[type])]
        except sqlite3.OperationalError:
            return []

    @staticmethod
    def getTeams():
        try:
            return [team[0] for team in
                DbQueries.db.execute("SELECT team_name FROM team")]
        except sqlite3.OperationalError:
            return []

    @staticmethod
    def getMatchesByTeam(team):
        try: 
            home = [f"Home VS {away_team} ({match_id})" for away_team, match_id in 
                DbQueries.db.execute("SELECT away_team, match_id FROM PARTICIPATION\
                    WHERE home_team = ? ORDER BY away_team", [team])
            ]
            away = [f"Away VS {home_team} ({match_id})" for home_team, match_id in 
                DbQueries.db.execute("SELECT home_team, match_id FROM PARTICIPATION\
                    WHERE away_team = ? ORDER BY home_team", [team])
            ]
            return home + away
        except sqlite3.OperationalError:
            return []

    @staticmethod
    def getRefPositions():
        return ["Head", "Assistant", "Fourth"]

    @staticmethod
    def getPositions():
        return [
            "ATT", "MID", "DEF", "GK"
        ]
    
    @staticmethod
    def getStatsTypes():
        return ["Goal", "Assist", "Own Goal",
            "Foul Kick", "Foul Commited", 
            "Penalty Kick", "Penalty Commited", 
            "Offside", "Corner Kick",
            "Yellow Card", "Red Card"
        ]
    
    @staticmethod
    def getStatByMatch(match):
        try:
            match_id = match.split("(")[1][:-1]
            return [f"{minute}min: {s_type} {p_name} {p_surname} ({id})" for minute, s_type, p_name, p_surname, id in
                DbQueries.db.execute("SELECT minute, stat_name, name, surname, statistic_id \
                    FROM statistic, player, people \
                    WHERE statistic.match_id = ? AND statistic.player_id = player.player_id AND people.people_id = player.people_id",
                    [match_id])
            ]
        except IndexError:
            #print("Failed to find statistic!")
            return []
        except sqlite3.OperationalError:
            return []

    @staticmethod
    def getCountries():
        return [country['name'] for country in
            json.load(open(QuerySelector.JSONs_PATH+'countries.json'))]
    
    @staticmethod
    def getLastYears(max_age=None, min_age=0, from_year=None):
        if not from_year: from_year = date.today().year - max_age if max_age else 1900
        return list(range(date.today().year-min_age, from_year, -1))



class DbQueries:

    ## Static Variables
    DB_PATH = './src/data/database.db'
    db = sqlite3.connect(DB_PATH)


    @staticmethod
    def submit(entries={}, method=None):        ## Needs a looot of Error Handling
        inputs = {entry: entries[entry].get() for entry in entries} # create a dict of {entry:input} ex. 'year':2021

        if method != None:
            error:str = method(inputs)
            if error:
                userAction = ctypes.windll.user32.MessageBoxW(0, error, "ERROR", 1)
                if userAction==2:
                    error = None    # User wants to cancel and clear the entries

            # Clear all GUI entries
            if not error and method != DbQueries.run_query: # If there are no errors and it's not the RunQuery page
                for entry in entries:
                    try: entries[entry].set('')  # for ComboBox
                    except AttributeError: entries[entry].delete(0,'end')   # for Entry

    
    # ****************************** INSERTIONS ******************************

    @staticmethod
    def insert_any(inputs:dict):
        for input in inputs:
            if inputs[input]=='':
                return f"Please add a value for {input.upper()}"
        return None

    @staticmethod
    def insert_people(inputs:dict):
        error = DbQueries.insert_any(inputs)
        if error: return error
        
        # Error Checking
        if len(inputs['id']) != 8:
            return "Please add an 8-chars Identity Card Number for this person."
        
        if len(inputs['tel'])<10 or not inputs['tel'][-10:].isdigit():
            return "The Phone number must be ending in a 10-digits number."
        
        # Queries
        date = '-'.join([inputs['year'], inputs['month'], inputs['day']])
        DbQueries.db.execute("INSERT INTO people (people_id, name, surname, birthdate, tel, nationality) VALUES (?,?,?, DATE(?), ?,?)",
            [inputs['id'], inputs['name'], inputs['surname'], date, inputs['tel'], inputs['nationality']])
        DbQueries.db.commit()

        print("Submited person!")
        return None
    
    @staticmethod
    def insert_player(inputs:dict):
        error = DbQueries.insert_people(inputs)
        if error: return error
        
        # Error Checking
        if len(inputs['card']) != 10:
            return "Please add an 10-chars Player Card Number for this person."

        # Queries
        DbQueries.db.execute("INSERT INTO player (player_id, people_id,team_name, position) VALUES (?,?,?,?)",
            [inputs['card'], inputs['id'], inputs['team'], inputs['position']])
        DbQueries.db.commit()

        print("Submited player!")
        return None

    @staticmethod
    def insert_referee(inputs:dict):
        error = DbQueries.insert_people(inputs)
        if error: return error
        
        # Error Checking
        if len(inputs['card']) != 10:
            return "Please add an 10-chars Referee Card Number for this person."

        # Queries
        DbQueries.db.execute("INSERT INTO referee (referee_id, people_id, type) VALUES (?,?,?)",
            [inputs['card'], inputs['id'], inputs['type']])
        DbQueries.db.commit()

        print("Submited referee!")
        return None

    @staticmethod
    def insert_team(inputs:dict):
        error = DbQueries.insert_any(inputs)
        if error: return error

        date = inputs['founded'] + '-01-01'
        DbQueries.db.execute("INSERT INTO team (team_name, home, founded) VALUES (?,?, DATE(?))", [inputs['name'], inputs['home'], date])
        DbQueries.db.commit()

        print("Submited club!")
        return None

    @staticmethod
    def insert_match(inputs:dict):
        error = DbQueries.insert_any(inputs)
        if error: return error

        datetime = '-'.join([inputs[i] for i in ['year','month','day']]) +' '+ inputs['hour']+':00'

        DbQueries.db.execute("INSERT INTO match (datime, home_team_goals, away_team_goals) VALUES (DATETIME(?),?,?)",
            [datetime, inputs['home_score'], inputs['away_score']])
        
        match_id = DbQueries.db.execute("SELECT match_id FROM match").fetchall()[-1][0]

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
        
        print("Submited match!")
        return None

    @staticmethod
    def insert_stat(inputs:dict):
        error = DbQueries.insert_any(inputs)
        if error: return error

        inputs["player"] = inputs["player"].split("(")[1][:-1]
        inputs["match"] = inputs["match"].split("(")[1][:-1]
        print(inputs)
        DbQueries.db.execute("INSERT INTO statistic (player_id, match_id, minute, stat_name) VALUES (?, ?, ?, ?)",
            [inputs['player'], inputs['match'], inputs['minute'], inputs['stat_name']])
        DbQueries.db.commit()

        print("Submited statistic!")
        return None

    
    # ****************************** DELETIONS ******************************

    @staticmethod
    def delete_player(inputs:dict):
        player = inputs["player"]
        player_id = player.split(" (")[1][:-1] # split id from name and remove ( )
        try:
            people_id = QuerySelector.getPeopleIdFromPlayerId(player_id)[0].split("'")[1]
        except IndexError:
            print("Failed to remove person!")
            return
        try:
            DbQueries.db.execute("DELETE FROM player WHERE player_id = ?",
                [player_id])
            DbQueries.db.execute("DELETE FROM people WHERE people_id = ?",
                [people_id])
            DbQueries.db.execute("DELETE FROM statistic WHERE player_id = ?",
                [player_id])
            DbQueries.db.commit()
        except sqlite3.OperationalError:
            return

    @staticmethod
    def delete_referee(inputs:dict):
        referee = inputs["referee"]
        referee_id = referee.split(" (")[1][:-1] # split id from name and remove ( )
        try:
            people_id = str(QuerySelector.getPeopleIdFromRefereeId(referee_id)).split("\'")[1]
        except IndexError:
            #print("Failed to remove person!")
            return
        #print(referee_id, people_id)
        try:
            DbQueries.db.execute("DELETE FROM referee WHERE referee_id = ?",
                [referee_id])
            DbQueries.db.execute("DELETE FROM people WHERE people_id = ?",
                [people_id])
            DbQueries.db.commit()
        except sqlite3.OperationalError:
            return

    @staticmethod
    def delete_team(inputs:dict):
        team = inputs["team"]
        DbQueries.db.execute("DELETE FROM team WHERE team_name = ?", [team])
        for player in QuerySelector.getPlayersByTeam(team):
            DbQueries.db.execute("UPDATE player SET team_name=NULL WHERE team_name=?", [team])
        for match in QuerySelector.getMatchesByTeam(team):
            DbQueries.delete_match({"match":match})
        DbQueries.db.commit()

    @staticmethod
    def delete_match(inputs:dict):
        try:
            match_id:str = inputs["match"].split("(")[1][:-1]
            DbQueries.db.execute("DELETE FROM participation WHERE match_id = ?", [match_id])
            DbQueries.db.execute("DELETE FROM match WHERE match_id = ?",  [match_id])
            DbQueries.db.execute("DELETE FROM statistic WHERE match_id = ?",  [match_id])
            DbQueries.db.commit()
        except IndexError:
            print("Failed to remove match!")
            return

    @staticmethod
    def delete_stat(inputs:dict):
        statistic = inputs["statistic"]
        try:
            statistic_id = statistic.split("(")[1][:-1]
            print(statistic_id)
            DbQueries.db.execute("DELETE FROM statistic WHERE statistic_id = ?",
            [statistic_id])
            DbQueries.db.commit()
        except IndexError:
            #print("Failed to remove statistic!")
            return
        except sqlite3.OperationalError:
            return
            
    @staticmethod
    def run_query(inputs:dict):
        print("Submited Query!")
        query = inputs['query']

        try:
            data = DbQueries.db.execute(query).fetchall()
            print(*data, sep='\n')
        except Exception as e:
            print(e)
