class QuerySelector():
    def __init__(self):
        pass

    @staticmethod
    def submit(inputs: dict, page=None):
        QuerySelector.slctTable(page)
        for func in inputs:
            print(func+":", inputs[func].get())
            inputs[func].delete(0,'end')

    @staticmethod
    def slctTable(page):
        print("\nSubmited", page)
    

    
    @staticmethod
    def getTeams():
        return ("Team1", "Team2", "Team3", "Team4", "Team5", "Team6", "Team7", "Team8", "Team9", "Team10")

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