import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.DbQueries import QuerySelector

class DeleteStatPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        self.create_team_selector().grid(row = 2, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        self.match_selector = self.create_match_selector("")
        self.match_selector.grid(row = 12, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        self.statistic_selector = self.create_statistic_selector("")
        self.statistic_selector.grid(row = 22, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        self.submitButton.grid(row = 32, column = 0)

    def onSubmit(self):
        super().onSubmit('delete_stat')

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

        print(team)
        matchSelector = ttk.Combobox(contentFrame, state = "readonly", width = 30)
        matchSelector["values"] = QuerySelector.getMatchesByTeam(team)
        self.inputs["match"] = matchSelector

        matchSelectorButton = ttk.Button(contentFrame, text = "Select",
                        command= self.select_match)
        
        matchLabel.grid(row = 0, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        matchSelector.grid(row = 1, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        matchSelectorButton.grid(row = 2, column = 0, columnspan = 4, padx = 10, sticky = tk.W)

        return contentFrame

    def create_statistic_selector(self, match):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")
        statisticLabel = ttk.Label(contentFrame, text = "Select statistic")

        print(match)
        statisticSelector = ttk.Combobox(contentFrame, state = "readonly", width = 30)
        statisticSelector["values"] = QuerySelector.getStatByMatch(match)
        self.inputs["statistic"] = statisticSelector

        statisticLabel.grid(row = 0, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        statisticSelector.grid(row = 1, column = 0, columnspan = 4, padx = 10, sticky = tk.W)

        return contentFrame

    def select_team(self):
        team = {func: self.inputs[func].get() for func in self.inputs}["team"]
        self.match_selector.destroy()
        self.match_selector = self.create_match_selector(team)
        self.match_selector.grid(row = 12, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)

    def select_match(self):
        match = {func: self.inputs[func].get() for func in self.inputs}["match"]
        self.statistic_selector.destroy()
        self.statistic_selector = self.create_statistic_selector(match)
        self.statistic_selector.grid(row = 22, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
