from msilib.schema import ControlEvent
import tkinter as tk
import tkinter.ttk as ttk
from libraries.Autocomplete.AutocompleteEntry import AutocompleteCombobox, AutocompleteEntry
from libraries.Checkbox.Combopicker import Combopicker 
from libraries.MainFrame import MainFrame
from libraries.dbIO.QuerySelector import QuerySelector

class AddPlayerPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        tk.Label(self, text="Add Player").grid(row=1, column=1)

        self.createPersonalInfoFrame()
        self.createBirthdayFrame()
        self.createAthleteCardFrame()

    def createPersonalInfoFrame(self):
        tk.Label(self, text = "Personal Info").grid(row = 2, column = 0, sticky = tk.W)
        contentFrame = ttk.Frame(self, borderwidth = 5, relief = "ridge")

        nameLabel = ttk.Label(contentFrame, text = "Name")
        nameEntry = ttk.Entry(contentFrame)
        nameEntry.focus_set()

        surnameLabel = ttk.Label(contentFrame, text = "Surname")
        surnameEntry = ttk.Entry(contentFrame)

        fatherNameLabel = ttk.Label(contentFrame, text = "Father's Name")
        fatherNameEntry = ttk.Entry(contentFrame)

        idCardLabel = ttk.Label(contentFrame, text = "Identity Card Number")
        idCardEntry = ttk.Entry(contentFrame)

        positionsLabel = ttk.Label(contentFrame, text = "Positions")
        positionsEntry = Combopicker(contentFrame, values = ["ST", "CF", "LW", "RW", 
                                                "LM", "CM", "CAM", "CDM", "RM",
                                                "LWB", "LB", "CB", "RB", "RWB", "GK"])

        teamLabel = ttk.Label(contentFrame, text = "Team")
        teamSelectorEntry = AutocompleteEntry(contentFrame)
        teamSelector = AutocompleteCombobox(contentFrame)
        teamSelector.set_completion_list(QuerySelector.getTeams())

        contentFrame.grid(row = 3, column = 0, columnspan = 8, rowspan = 6, sticky = tk.W)        

        nameLabel.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        nameEntry.grid(row = 3, column = 0, columnspan = 2, padx = 10)
        
        surnameLabel.grid(row = 2, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        surnameEntry.grid(row = 3, column = 2, columnspan = 2, padx = 10)

        fatherNameLabel.grid(row = 2, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        fatherNameEntry.grid(row = 3, column = 4, columnspan = 2, padx = 10, sticky = tk.W)     

        idCardLabel.grid(row = 5, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        idCardEntry.grid(row = 6, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        positionsLabel.grid(row = 5, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        positionsEntry.grid(row = 6, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        teamLabel.grid(row = 5, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        teamSelectorEntry.grid(row = 6, column = 4, columnspan = 2, padx = 10)
        teamSelector.grid(row = 6, column = 4, columnspan = 2, padx = 10)

    def createBirthdayFrame(self):
        tk.Label(self, text = "Birthday").grid(row = 9, column = 0, sticky = tk.W)
        contentFrame = ttk.Frame(self, borderwidth = 5, relief = "ridge")

        ageYear = ttk.Label(contentFrame, text = "Year")
        selectedYear = tk.IntVar()
        yearSelector = ttk.Combobox(contentFrame, textvariable = selectedYear, state = "readonly")
        yearSelector["values"] = [year for year in range(1970, 2008, 1)]
        
        # TODO : CREATE FUNTCION THAT RETURNS ALL YEARS FROM 1970 TILL CURRENT_YEAR - 15
        
        ageMonth = ttk.Label(contentFrame, text = "Month")
        selectedMonth = tk.StringVar()
        monthSelector = ttk.Combobox(contentFrame, textvariable = selectedMonth, state = "readonly")
        monthSelector["values"] = [month for month in ["JAN", "FEB", "MAR", "APR", "JUN", 
                                                            "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]]
        # TODO : CREATE FUNTCION THAT RETURNS ALL MONTHS

        ageDay = ttk.Label(contentFrame, text = "Day")
        selectedDay = tk.IntVar()
        daySelector = ttk.Combobox(contentFrame, textvariable = selectedDay, state = "readonly")
        daySelector["values"] = [day for day in range(1, 32, 1)]

         # TODO : CREATE FUNTCION THAT RETURNS DAYS OF SELECTED MONTH

        contentFrame.grid(row = 10, column = 0, columnspan = 6, rowspan = 4, sticky = tk.W) 

        ageYear.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        yearSelector.grid(row = 1, column = 0, columnspan = 2, padx=10)

        ageMonth.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        monthSelector.grid(row = 1, column = 2, columnspan = 2, padx=10)

        ageDay.grid(row = 0, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        daySelector.grid(row = 1, column = 4, columnspan = 2, padx=10)

    def createAthleteCardFrame(self):
        tk.Label(self, text = "Birthday").grid(row = 14, column = 0, sticky = tk.W)
        contentFrame = ttk.Frame(self, borderwidth = 5, relief = "ridge")

        athleteCardLabel = ttk.Label(contentFrame, text = "Athlete Card Number")
        athleteCardEntry = ttk.Entry(contentFrame)

        expireYearLabel = ttk.Label(contentFrame, text = "Year")
        selectedExpireYear = tk.IntVar()
        expireYearSelector = ttk.Combobox(contentFrame, textvariable = selectedExpireYear, state = "readonly")
        expireYearSelector["values"] = [year for year in range(1970, 2008, 1)]
        
        # TODO : CREATE FUNTCION THAT RETURNS ALL YEARS FROM 1970 TILL CURRENT_YEAR - 15
        
        expireMonthLabel = ttk.Label(contentFrame, text = "Month")
        selectedExpireMonth = tk.StringVar()
        expireMonthSelector = ttk.Combobox(contentFrame, textvariable = selectedExpireMonth, state = "readonly")
        expireMonthSelector["values"] = [month for month in ["JAN", "FEB", "MAR", "APR", "JUN", 
                                                            "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]]
        # TODO : CREATE FUNTCION THAT RETURNS ALL MONTHS

        expireDayLabel = ttk.Label(contentFrame, text = "Day")
        selectedExpireDay = tk.IntVar()
        expireDaySelector = ttk.Combobox(contentFrame, textvariable = selectedExpireDay, state = "readonly")
        expireDaySelector["values"] = [day for day in range(1, 32, 1)]

         # TODO : CREATE FUNTCION THAT RETURNS DAYS OF SELECTED MONTH

        contentFrame.grid(row = 15, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W) 

        athleteCardLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        athleteCardEntry.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        expireYearLabel.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        expireYearSelector.grid(row = 3, column = 0, columnspan = 2, padx=10, sticky = tk.W)

        expireMonthLabel.grid(row = 2, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        expireMonthSelector.grid(row = 3, column = 2, columnspan = 2, padx=10, sticky = tk.W)

        expireDayLabel.grid(row = 2, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        expireDaySelector.grid(row = 3, column = 4, columnspan = 2, padx=10, sticky = tk.W)
