class QuerySelector():
    def __init__(self):
        pass

    @staticmethod
    def getTeams():
        return ("Team1", "Team2", "Team3", "Team12", "Team15", "Team100", "TeamABCDE", "Team1234ABCD", "Team7", "Team8")

    @staticmethod
    def getPositions():
        return ("Attacker", "Midfielder", "Defender", "Goalkeeper")

    @staticmethod
    def getSpecificPositions():
        return (
            "ST", "CF", "LW", "RW", 
            "LM", "CM", "CAM", "CDM", "RM",
            "LWB", "LB", "CB", "RB", "RWB", "GK"
        )