import json
from datetime import date
from libraries.dbIO.DbQueries import DbQueries

class QuerySelector:

    ## Static Variables
    JSONs_PATH = './src/libraries/JsonFiles/'
    

    @staticmethod
    def getTeams():
        return [club[0] for club in DbQueries.db.execute("SELECT name FROM clubs")]
    
    @staticmethod
    def getRefPositions():
        return ["headref#0", "assistref#1", "assistref#2", "fourthref#4"]
    
    @staticmethod
    def getReferees():
        return [ref[0] for ref in DbQueries.db.execute("SELECT * FROM referees")]

    @staticmethod
    def getPositions():
        # return ["Attacker", "Midfielder", "Defender", "Goalkeeper"]
        return [
            "ST", "CF", "LW", "RW",
            "LM", "CM", "CAM", "CDM", "RM",
            "LWB", "LB", "CB", "RB", "RWB",
            "GK"]
    
    @staticmethod
    def getCountries():
        return [country['name'] for country in
            json.load(open(QuerySelector.JSONs_PATH+'countries.json'))]
    
    @staticmethod
    def getLastYears(max_age=None, min_age=0, from_year=None):
        if not from_year: from_year = date.today().year - max_age if max_age else 1900
        return list(range(date.today().year-min_age, from_year, -1))

