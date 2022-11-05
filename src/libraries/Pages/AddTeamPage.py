import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame

class AddTeamPage(MainFrame):
    def __init__(self, master, personType=""):
        MainFrame.__init__(self, master)

        self.teamInfoFrame = self.createTeamInfoFrame(self.scrollable_frame)
        tk.Label(self.scrollable_frame, text = "Team Info").grid(row = 2, column = 0, sticky = tk.W)
        self.teamInfoFrame.grid(row = 3, column = 0, columnspan = 6, rowspan = 4, sticky = tk.W)

    def createTeamInfoFrame(self, container):
        contentFrame = ttk.Frame(container, borderwidth = 5, relief = "ridge")

        nameLabel = ttk.Label(contentFrame, text = "Name")
        nameEntry = ttk.Entry(contentFrame)
        nameEntry.focus_set()

        stadiumLabel = ttk.Label(contentFrame)
        stadiumEntry = ttk.Entry(contentFrame)

        foundationYear = ttk.Label(contentFrame, text = "FoundationYear")
        selectedYear = tk.IntVar()
        yearSelector = ttk.Combobox(contentFrame, textvariable = selectedYear, state = "readonly")
        yearSelector["values"] = [year for year in range(1970, 2022, 1)]
        
        # TODO : CREATE FUNTCION THAT RETURNS ALL YEARS FROM 1970 TILL CURRENT_YEAR - 15
        
        foundationMonth = ttk.Label(contentFrame, text = "Foundation Month")
        selectedMonth = tk.StringVar()
        monthSelector = ttk.Combobox(contentFrame, textvariable = selectedMonth, state = "readonly")
        monthSelector["values"] = [month for month in ["JAN", "FEB", "MAR", "APR", "JUN", 
                                                            "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]]
        # TODO : CREATE FUNTCION THAT RETURNS ALL MONTHS

        foundationDay = ttk.Label(contentFrame, text = "Foundation Day")
        selectedDay = tk.IntVar()
        daySelector = ttk.Combobox(contentFrame, textvariable = selectedDay, state = "readonly")
        daySelector["values"] = [day for day in range(1, 32, 1)]

        nameLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        nameEntry.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        
        stadiumLabel.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        stadiumEntry.grid(row = 1, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        foundationYear.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        yearSelector.grid(row = 3, column = 0, columnspan = 2, padx=10, sticky = tk.W)

        foundationMonth.grid(row = 2, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        monthSelector.grid(row = 3, column = 2, columnspan = 2, padx=10, sticky = tk.W)

        foundationDay.grid(row = 2, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        daySelector.grid(row = 3, column = 4, columnspan = 2, padx=10, sticky = tk.W)

        return contentFrame