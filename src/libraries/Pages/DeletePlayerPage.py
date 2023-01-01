import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.DbQueries import QuerySelector

class DeletePlayerPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        self.create_team_selector().grid(row = 2, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        self.player_selector = self.create_player_selector("")
        self.player_selector.grid(row = 12, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        self.submitButton.grid(row = 50, column = 0)

    def onSubmit(self):
        super().onSubmit('delete_player')

    def create_team_selector(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        teamLabel = ttk.Label(contentFrame, text = "Select team")
        teamSelector = ttk.Combobox(contentFrame, state = "readonly", width = 30)
        teamSelector["values"] = QuerySelector.getTeams()
        teamSelector.focus_set()
        self.inputs["team"] = teamSelector

        teamSelectorButton = ttk.Button(contentFrame, text = "Select",
                        command= self.select_team)

        teamLabel.grid(row = 0, column = 0, columnspan = 6, padx = 10, sticky = tk.W)
        teamSelector.grid(row = 1, column = 0, columnspan = 6, padx = 10, sticky = tk.W)
        teamSelectorButton.grid(row = 2, column = 0, columnspan = 6, padx = 10, sticky = tk.W)

        return contentFrame

    def create_player_selector(self, team):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")
        playerLabel = ttk.Label(contentFrame, text = "Select player")

        playerSelector = ttk.Combobox(contentFrame, state = "readonly", width = 30)
        playerSelector["values"] = QuerySelector.getPlayersByTeam(team)
        self.inputs["player"] = playerSelector
        
        playerLabel.grid(row = 0, column = 0, columnspan = 6, padx = 10, sticky = tk.W)
        playerSelector.grid(row = 1, column = 0, columnspan = 6, padx = 10, sticky = tk.W)

        return contentFrame

    def select_team(self):
        team = {func: self.inputs[func].get() for func in self.inputs}["team"]
        self.player_selector.destroy()
        self.player_selector = self.create_player_selector(team)
        self.player_selector.grid(row = 12, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)