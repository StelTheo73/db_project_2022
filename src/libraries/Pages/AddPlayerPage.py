import tkinter as tk
import tkinter.ttk as ttk
from libraries.Pages.AddPersonPage import AddPersonPage
from libraries.dbIO.DbQueries import QuerySelector

class AddPlayerPage(AddPersonPage):
    def __init__(self, master):
        AddPersonPage.__init__(self, master, personType="Player")

        tk.Label(self.scrollable_frame, text = "Team Info").grid(row = 17, column = 0, sticky = tk.W)
        self.createTeamInfoFrame().grid(row = 18, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
    
        self.submitButton.grid(row = 28, column = 0)

    def createTeamInfoFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        teamLabel = ttk.Label(contentFrame, text = "Team")
        teamSelector = ttk.Combobox(contentFrame, state = "readonly")
        teamSelector["values"] = QuerySelector.getTeams()
        self.inputs["team"] = teamSelector
        
        positionsLabel = ttk.Label(contentFrame, text = "Position")
        positionSelector = ttk.Combobox(contentFrame, state = "readonly")
        positionSelector["values"] = QuerySelector.getPositions()
        self.inputs["position"] = positionSelector
 
        teamLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        teamSelector.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        positionsLabel.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        positionSelector.grid(row = 1, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame
