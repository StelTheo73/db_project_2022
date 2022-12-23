import json
from datetime import date
from libraries.dbIO.DbQueries import DbQueries

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
    
    def getPeopleIdFromPlayerId(player_id):
        return [f"{people_id}" for people_id in
            DbQueries.db.execute("SELECT people_id FROM people, player WHERE people.people_id = player.people_id AND player_id = ?",[player_id])]

    def getPeopleIdFromRefereeId(referee_id):
        return [f"{people_id}" for people_id in
            DbQueries.db.execute("SELECT people_id FROM people, referee WHERE people.people_id = referee.referee_id AND referee_id = ?",[referee_id])]

    @staticmethod
    def getPlayers():
        return [f"{lName} {fName} ({id})" for lName,fName,id in
            DbQueries.db.execute("SELECT surname, name, player_id FROM player,people WHERE player.people_id=people.people_id ORDER BY surname, name, player_id")]
    
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

