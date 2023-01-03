import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.DbQueries import QuerySelector

class AddStatPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        self.team_selector = self.create_team_selector()
        self.team_selector.grid(row = 2, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        self.match_selector = self.create_match_selector("", getFocus = False)
        self.match_selector.grid(row = 12, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        self.statistic_info = self.create_statistic_info("", getFocus = False)
        self.statistic_info.grid(row = 22, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        self.submitButton.grid(row = 32, column = 0)

    def onSubmit(self):
        super().onSubmit('stat')

    def create_team_selector(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        teamLabel = ttk.Label(contentFrame, text = "Select team")
        teamSelector = ttk.Combobox(contentFrame, state = "readonly", width = 30)
        teamSelector["values"] = QuerySelector.getTeams()
        teamSelector.focus_set()
        self.inputs["team"] = teamSelector

        teamSelectorButton = ttk.Button(contentFrame, text = "Select",
                        command= self.select_team)

        teamLabel.grid(row = 0, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        teamSelector.grid(row = 1, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        teamSelectorButton.grid(row = 2, column = 0, columnspan = 4, padx = 10, sticky = tk.W)

        return contentFrame

    def create_match_selector(self, team, getFocus = True):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")
        matchLabel = ttk.Label(contentFrame, text = "Select match")

        matchSelector = ttk.Combobox(contentFrame, state = "readonly", width = 30)
        matchSelector["values"] = QuerySelector.getMatchesByTeam(team)
        self.inputs["match"] = matchSelector
        
        if getFocus:
            matchSelector.focus_set()

        matchSelectorButton = ttk.Button(contentFrame, text = "Select",
                        command= self.select_match)
        
        matchLabel.grid(row = 0, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        matchSelector.grid(row = 1, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        matchSelectorButton.grid(row = 2, column = 0, columnspan = 4, padx = 10, sticky = tk.W)

        return contentFrame

    def create_statistic_info(self, team, getFocus = True):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")
        
        playerLabel = ttk.Label(contentFrame, text = "Player")
        playerSelector = ttk.Combobox(contentFrame, state = "readonly")
        playerSelector["values"] = QuerySelector.getPlayersByTeam(team)
        self.inputs["player"] = playerSelector
        
        if getFocus:
            playerSelector.focus_set()

        minuteLabel = ttk.Label(contentFrame, text = "Minute")
        minuteSelector = ttk.Combobox(contentFrame, state = "readonly")
        minuteSelector["values"] = [str(minute).zfill(2) for minute in range(0, 100)]
        self.inputs["minute"] = minuteSelector

        statLabel = ttk.Label(contentFrame, text = "Type")
        statSelector = ttk.Combobox(contentFrame, state = "readonly")
        statSelector["values"] = QuerySelector.getStatsTypes()
        self.inputs["stat_name"] = statSelector

        playerLabel.grid(row = 0, column = 0, columnspan = 8, padx = 10, sticky = tk.W)
        playerSelector.grid(row = 1, column = 0, columnspan = 8, padx = 10, sticky = tk.W)
        minuteLabel.grid(row = 2, column = 0, columnspan = 8, padx = 10, sticky = tk.W)
        minuteSelector.grid(row = 3, column = 0, columnspan = 8, padx = 10, sticky = tk.W)
        statLabel.grid(row = 4, column = 0, columnspan = 8, padx = 10, sticky = tk.W)
        statSelector.grid(row = 5, column = 0, columnspan = 8, padx = 10, sticky = tk.W)

        return contentFrame

    def select_team(self):
        team = {func: self.inputs[func].get() for func in self.inputs}["team"]
        self.match_selector.destroy()
        self.match_selector = self.create_match_selector(team)
        self.match_selector.grid(row = 12, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        
    def select_match(self):
        team = {func: self.inputs[func].get() for func in self.inputs}["team"]
        match = {func: self.inputs[func].get() for func in self.inputs}["match"]
        self.statistic_info.destroy()
        self.statistic_info = self.create_statistic_info(team)
        self.statistic_info.grid(row = 22, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)

