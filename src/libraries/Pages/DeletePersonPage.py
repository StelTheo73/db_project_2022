import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.QuerySelector import QuerySelector

class DeletePersonPage(MainFrame):
    def __init__(self, master, personType:str):
        MainFrame.__init__(self, master)
        self.personType = personType
        self.create_team_selector().grid(row = 2, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)

    def create_team_selector(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        teamLabel = ttk.Label(contentFrame, text = "Select team")
        teamSelector = ttk.Combobox(contentFrame, state = "readonly")
        teamSelector["values"] = QuerySelector.getTeams()
        self.inputs["team"] = teamSelector

        teamSelectorButton = ttk.Button(contentFrame, text = "Select",
                        command= self.select_team)

        teamLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        teamSelector.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        teamSelectorButton.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame

    def create_player_selector(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")
        playerLabel = ttk.Label(contentFrame, text = "Select player")
        
        team = {func: self.inputs[func].get() for func in self.inputs}["team"]
        print(team)
        playerSelector = ttk.Combobox(contentFrame, state = "readonly")
        playerSelector["values"] = QuerySelector.getPlayersByTeam(team)
        self.inputs["player"] = playerSelector
        
        playerLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        playerSelector.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        #playerSelectorButton.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)


        return contentFrame

    def select_team(self):
        self.create_player_selector().grid(row = 4, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)