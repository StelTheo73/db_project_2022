import tkinter as tk
import tkinter.ttk as ttk
from libraries.Pages.AddPersonPage import AddPersonPage
from libraries.dbIO.QuerySelector import QuerySelector

class AddPlayerPage(AddPersonPage):
    def __init__(self, master):
        AddPersonPage.__init__(self, master, personType="Player")

        self.teamInfoFrame = self.createTeamInfoFrame()

        tk.Label(self.scrollable_frame, text = "Team Info").grid(row = 17, column = 0, sticky = tk.W)
        self.teamInfoFrame.grid(row = 18, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
    
    def createTeamInfoFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        teamLabel = ttk.Label(contentFrame, text = "Team")
        teamSelector = ttk.Combobox(contentFrame, state = "readonly")
        teamSelector["values"] = QuerySelector.getTeams()
        self.inputs["club"] = teamSelector
        
        positionsLabel = ttk.Label(contentFrame, text = "Position")
        selectedPosition = tk.StringVar()
        # https://stackoverflow.com/questions/37414600/python-tkinter-using-a-textvariable-in-a-combobox-seems-useless
        positionSelector = ttk.Combobox(contentFrame, textvariable = selectedPosition, state = "readonly")
        positionSelector["values"] = QuerySelector.getPositions() # WTF Stel! I use QuerySelector for other shit
        self.inputs["position"] = positionSelector
 
        teamLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        teamSelector.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        positionsLabel.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        positionSelector.grid(row = 1, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame
