import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.DbQueries import QuerySelector

class DeleteMatchPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        self.create_team_selector().grid(row = 2, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        self.match_selector = self.create_match_selector("")
        self.match_selector.grid(row = 12, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        self.submitButton.grid(row = 50, column = 0)

    def onSubmit(self):
        super().onSubmit('delete_match')

    def create_team_selector(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        teamLabel = ttk.Label(contentFrame, text = "Select team")
        teamSelector = ttk.Combobox(contentFrame, state = "readonly", width = 30)
        teamSelector["values"] = QuerySelector.getTeams()
        teamSelector.focus_get()
        self.inputs["team"] = teamSelector

        teamSelectorButton = ttk.Button(contentFrame, text = "Select",
                        command= self.select_team)

        teamLabel.grid(row = 0, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        teamSelector.grid(row = 1, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        teamSelectorButton.grid(row = 2, column = 0, columnspan = 4, padx = 10, sticky = tk.W)

        return contentFrame

    def create_match_selector(self, team):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")
        matchLabel = ttk.Label(contentFrame, text = "Select match")

        matchSelector = ttk.Combobox(contentFrame, state = "readonly", width = 30)
        matchSelector["values"] = QuerySelector.getMatchesByTeam(team)
        self.inputs["match"] = matchSelector
        
        matchLabel.grid(row = 0, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        matchSelector.grid(row = 1, column = 0, columnspan = 4, padx = 10, sticky = tk.W)

        return contentFrame

    def select_team(self):
        team = {func: self.inputs[func].get() for func in self.inputs}["team"]
        self.match_selector.destroy()
        self.match_selector = self.create_match_selector(team)
        self.match_selector.grid(row = 12, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)