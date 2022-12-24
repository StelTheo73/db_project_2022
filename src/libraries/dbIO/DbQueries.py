import sqlite3
import json
from datetime import date

class QuerySelector:

    ## Static Variables
    JSONs_PATH = './src/libraries/JsonFiles/'
    
    @staticmethod
    def getMatches():
        return [f"{home}-{away} (match#{id})" for id,home,away in
            DbQueries.db.execute("SELECT match.match_id, home_team, away_team FROM match,participation WHERE match.match_id=participation.match_id")]
    
    @staticmethod
    def getPeopleId(id):
        return [f"{people_id}" for people_id in
            DbQueries.db.execute("SELECT people_id FROM people WHERE people_id = ?",[id])]
    
    @staticmethod
    def getPeopleIdFromPlayerId(player_id):
        return [f"{people_id}" for people_id in
            DbQueries.db.execute("SELECT people.people_id FROM people, player WHERE people.people_id = player.people_id AND player.player_id = ?",[player_id])]

    @staticmethod
    def getPeopleIdFromRefereeId(referee_id):
        return [f"{people_id}" for people_id in
            DbQueries.db.execute("SELECT people.people_id FROM people, referee WHERE people.people_id = referee.people_id AND referee_id = ?",[referee_id])]

    @staticmethod
    def getPlayers():
        return [f"{lName} {fName} ({id})" for lName,fName,id in
            DbQueries.db.execute("SELECT surname, name, player_id FROM player,people WHERE player.people_id=people.people_id ORDER BY surname, name, player_id")]
    
    @staticmethod
    def getPlayersByTeam(team):
        return [f"{lName} {fName} ({id})" for lName,fName,id in
            DbQueries.db.execute("SELECT surname, name, player_id FROM player,people WHERE player.people_id=people.people_id AND player.team_name=? ORDER BY surname, name, player_id",[team])]

    @staticmethod
    def getReferees():
        return [f"{lName} {fName} ({id})" for lName,fName,id in
            DbQueries.db.execute("SELECT surname, name, referee_id FROM referee,people  WHERE referee.people_id=people.people_id ORDER BY surname, name, referee_id")]
    
    @staticmethod
    def getRefereesByType(type):
        return [f"{lName} {fName} ({id})" for lName,fName,id in
            DbQueries.db.execute("SELECT surname, name, referee_id FROM referee,people  WHERE referee.people_id=people.people_id AND referee.type=? ORDER BY surname, name, referee_id",[type])]

    @staticmethod
    def getTeams():
        return [team[0] for team in
            DbQueries.db.execute("SELECT team_name FROM team")]

    @staticmethod
    def getMatchesByTeam(team):
        home = [f"Home VS {away_team} ({match_id})" for away_team, match_id in 
            DbQueries.db.execute("SELECT away_team, match_id FROM PARTICIPATION\
                WHERE home_team = ? ORDER BY away_team", [team])
        ]
        away = [f"Away VS {home_team} ({match_id})" for home_team, match_id in 
            DbQueries.db.execute("SELECT home_team, match_id FROM PARTICIPATION\
                WHERE away_team = ? ORDER BY home_team", [team])
        ]
        return home + away

    @staticmethod
    def getRefPositions():
        return ["Head", "Assistant", "Fourth"]

    @staticmethod
    def getPositions():
        return [
            "ST", "CF", "LW", "RW",
            "LM", "CM", "CAM", "CDM", "RM",
            "LWB", "LB", "CB", "RB", "RWB",
            "GK"]
    
    @staticmethod
    def getStatsTypes():
        return ["Goal", "Assist", "Foul", "Penalty", "Offside", "Corner"]
    
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
        inputs = {func: entries[func].get() for func in entries}
        if method != DbQueries.run_query:
            for func in entries:    # Clear entries
                try: entries[func].set('')  # for ComboBox
                except AttributeError: entries[func].delete(0,'end')   # for Entry

        if method != None: method(inputs)
    
    @staticmethod
    def insert_player(inputs):
        print("Submited player!")

        DbQueries.insert_people(inputs)

        DbQueries.db.execute("INSERT INTO player (player_id, people_id,team_name, position) VALUES (?,?,?,?)",
            [inputs['card'], inputs['id'], inputs['team'], inputs['position']])
        DbQueries.db.commit()
    
    @staticmethod
    def delete_player(inputs):
        player = inputs["player"]
        player_id = player.split(" (")[1][:-1] # split id from name and remove ( )
        try:
            people_id = str(QuerySelector.getPeopleIdFromPlayerId(player_id)).split("\'")[1]
        except IndexError:
            print("Failed to remove person!")
            return
        print(player_id, people_id)
        DbQueries.db.execute("DELETE FROM player WHERE player_id = ?",
            [player_id])
        DbQueries.db.execute("DELETE FROM people WHERE people_id = ?",
            [people_id])
        DbQueries.db.commit()

    @staticmethod
    def insert_referee(inputs):
        print("Submited referee!")

        DbQueries.insert_people(inputs)

        DbQueries.db.execute("INSERT INTO referee (referee_id, people_id, type) VALUES (?,?,?)",
            [inputs['card'], inputs['id'], inputs['type']])
        DbQueries.db.commit()
    
    @staticmethod
    def delete_referee(inputs):
        referee = inputs["referee"]
        referee_id = referee.split(" (")[1][:-1] # split id from name and remove ( )
        try:
            people_id = str(QuerySelector.getPeopleIdFromRefereeId(referee_id)).split("\'")[1]
        except IndexError:
            print("Failed to remove person!")
            return
        print(referee_id, people_id)
        DbQueries.db.execute("DELETE FROM referee WHERE referee_id = ?",
            [referee_id])
        DbQueries.db.execute("DELETE FROM people WHERE people_id = ?",
            [people_id])
        DbQueries.db.commit()

    @staticmethod
    def insert_people(inputs):
        print("Submited person!")

        date = '-'.join([inputs['year'], inputs['month'], inputs['day']])
        DbQueries.db.execute("INSERT INTO people (people_id, name, surname, birthdate, tel, nationality) VALUES (?,?,?, DATE(?), ?,?)",
            [inputs['id'], inputs['name'], inputs['surname'], date, inputs['tel'], inputs['nationality']])
        DbQueries.db.commit()
    
    @staticmethod
    def insert_team(inputs):
        print("Submitedteam!")

        date = inputs['founded'] + '-01-01'
        DbQueries.db.execute("INSERT INTO team (club_name, home, founded) VALUES (?,?, DATE(?))", [inputs['name'], inputs['home'], date])
        DbQueries.db.commit()

    @staticmethod
    def delete_team(inputs):
        team_name = inputs["team"]
        print(team_name)
        DbQueries.db.execute("DELETE FROM team WHERE team_name = ?",
            [team_name])
        DbQueries.db.commit()

    @staticmethod
    def insert_match(inputs):
        print("Submited match!")

        datetime = '-'.join([inputs[i] for i in ['year','month','day']]) +' '+ inputs['hour']+':00'

        DbQueries.db.execute("INSERT INTO match (datime, home_goals, away_goals) VALUES (DATETIME(?),?,?)",
            [datetime, inputs['home_score'], inputs['away_score']])
        
        match_id = DbQueries.db.execute("SELECT match_id FROM match").fetchall()[-1][0]

        DbQueries.db.execute("INSERT INTO participation (match_id, home_team, away_team) VALUES (?,?,?)",
            [match_id, inputs['home_team'], inputs['away_team']])
        
        DbQueries.db.execute("INSERT INTO gameControl (match_id, referee_id) VALUES (?,?)",
            [match_id, inputs['head_ref']])

        DbQueries.db.execute("INSERT INTO gameControl (match_id, referee_id) VALUES (?,?)",
            [match_id, inputs['assist_ref_1']])

        DbQueries.db.execute("INSERT INTO gameControl (match_id, referee_id) VALUES (?,?)",
            [match_id, inputs['assist_ref_2']])

        DbQueries.db.execute("INSERT INTO gameControl (match_id, referee_id) VALUES (?,?)",
            [match_id, inputs['fourth_ref']])

        DbQueries.db.commit()

    @staticmethod
    def delete_match(inputs):
        match = inputs["match"]
        try:
            match_id = match.split("(")[1][:-1]
            print(match_id)
            DbQueries.db.execute("DELETE FROM participation WHERE match_id = ?",
            [match_id])
            DbQueries.db.execute("DELETE FROM match WHERE match_id = ?", 
            [match_id])
            DbQueries.db.commit()
        except IndexError:
            print("Failed to remove match!")

    @staticmethod
    def insert_stat(inputs):
        print("Submited statistic!")

        DbQueries.db.execute("INSERT INTO statistic (player_id, match_id, minute, stat_name) VALUES (?, ?, ?, ?)",
            [inputs['player'], inputs['match'], inputs['minute'], inputs['stat_name']])
        DbQueries.db.commit()


    @staticmethod
    def run_query(inputs):
        print("Submited Query!")
        query = inputs['query']

        try:
            data = DbQueries.db.execute(query).fetchall()
            print(*data, sep='\n')
        except Exception as e:
            print(e)
