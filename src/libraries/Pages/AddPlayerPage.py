import tkinter as tk
import tkinter.ttk as ttk
from libraries.Autocomplete.AutocompleteEntry import AutocompleteCombobox, AutocompleteEntry
from libraries.Pages.AddPersonPage import AddPersonPage
from libraries.dbIO.QuerySelector import QuerySelector

class AddPlayerPage(AddPersonPage):
    def __init__(self, master):
        AddPersonPage.__init__(self, master, personType = "Athlete")
        tk.Label(self.scrollable_frame, text="Add Player").grid(row=1, column=0, sticky = tk.W)

        self.teamInfoFrame = self.createTeamInfoFrame(self.scrollable_frame)

        tk.Label(self.scrollable_frame, text = "Team Info").grid(row = 17, column = 0, sticky = tk.W)
        self.teamInfoFrame.grid(row = 18, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)

    def createTeamInfoFrame(self, container):
        contentFrame = ttk.Frame(container, borderwidth = 5, relief = "ridge")

        teamLabel = ttk.Label(contentFrame, text = "Team")
        teamSelectorEntry = AutocompleteEntry(contentFrame)
        teamSelector = AutocompleteCombobox(contentFrame)
        teamSelector.set_completion_list(QuerySelector.getTeams())
        
        positionsLabel = ttk.Label(contentFrame, text = "Position")
        selectedPosition = tk.StringVar()
        positionSelector = ttk.Combobox(contentFrame, textvariable = selectedPosition)
        positionSelector["values"] = QuerySelector.getPositions()
 
        teamLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        teamSelectorEntry.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        teamSelector.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        positionsLabel.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        positionSelector.grid(row = 1, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame
