import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.QuerySelector import QuerySelector

class AddTeamPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        self.inputs = {}

        tk.Label(self.scrollable_frame, text="Add Team").grid(row=1, column=0, sticky = tk.W)

        self.teamInfoFrame = self.createTeamInfoFrame()
        tk.Label(self.scrollable_frame, text = "Team Info").grid(row = 2, column = 0, sticky = tk.W)
        self.teamInfoFrame.grid(row = 3, column = 0, columnspan = 6, rowspan = 4, sticky = tk.W)

    def onSubmit(self):
        super().onSubmit(self.inputs, 'club')

    def createTeamInfoFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        nameLabel = ttk.Label(contentFrame, text = "Name")
        nameEntry = ttk.Entry(contentFrame)
        self.inputs["name"] = nameEntry
        nameEntry.focus_set()

        stadiumLabel = ttk.Label(contentFrame, text = "Stadium")
        stadiumEntry = ttk.Entry(contentFrame)
        self.inputs["home"] = stadiumEntry

        foundationYear = ttk.Label(contentFrame, text = "FoundationYear")
        selectedYear = tk.IntVar()
        yearSelector = ttk.Combobox(contentFrame, textvariable = selectedYear, state = "readonly")
        yearSelector["values"] = QuerySelector.getLastYears() #[year for year in range(1900, 2022, 1)]
        self.inputs["founded"] = yearSelector
        

        nameLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        nameEntry.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        
        stadiumLabel.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        stadiumEntry.grid(row = 1, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        foundationYear.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        yearSelector.grid(row = 3, column = 0, columnspan = 2, padx=10, sticky = tk.W)

        return contentFrame