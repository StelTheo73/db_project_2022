import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.DbQueries import QuerySelector

class DeleteTeamPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        self.create_team_selector().grid(row = 2, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        self.submitButton.grid(row = 50, column = 0)

    def onSubmit(self):
        super().onSubmit('delete_team')

    def create_team_selector(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        teamLabel = ttk.Label(contentFrame, text = "Select team")
        teamSelector = ttk.Combobox(contentFrame, state = "readonly", width = 30)
        teamSelector["values"] = QuerySelector.getTeams()
        teamSelector.focus_set()
        self.inputs["team"] = teamSelector

        teamLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        teamSelector.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame
