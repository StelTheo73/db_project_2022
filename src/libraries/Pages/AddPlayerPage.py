from msilib.schema import ControlEvent
import tkinter as tk
import tkinter.ttk as ttk
from libraries.Autocomplete.AutocompleteEntry import AutocompleteCombobox, AutocompleteEntry
from libraries.MainFrame import MainFrame
from libraries.dbIO.QuerySelector import QuerySelector

class AddPlayerPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        tk.Label(self.scrollable_frame, text="Add Player").grid(row=1, column=1)

        self.personalInfoFrame = self.createPersonalInfoFrame(self.scrollable_frame)
        self.birthdayFrame = self.createBirthdayFrame(self.scrollable_frame)
        self.contactInfoFrame =  self.createContactInfoFrame(self.scrollable_frame)
        self.teamInfoFrame = self.createTeamInfoFrame(self.scrollable_frame)
        
        tk.Label(self.scrollable_frame, text = "Personal Info").grid(row = 2, column = 0, sticky = tk.W)
        self.personalInfoFrame.grid(row = 3, column = 0, columnspan = 8, rowspan = 4, sticky = tk.W)
        
        tk.Label(self.scrollable_frame, text = "Birthday").grid(row = 7, column = 0, sticky = tk.W)
        self.birthdayFrame.grid(row = 8, column = 0, columnspan = 6, rowspan = 2, sticky = tk.W)

        tk.Label(self.scrollable_frame, text = "Contact Info").grid(row = 10, column = 0, sticky = tk.W)
        self.contactInfoFrame.grid(row = 11, column = 0, columnspan = 6, rowspan = 6, sticky = tk.W) 

        tk.Label(self.scrollable_frame, text = "Team Info").grid(row = 17, column = 0, sticky = tk.W)
        self.teamInfoFrame.grid(row = 18, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)

    def createPersonalInfoFrame(self, container):
        contentFrame = ttk.Frame(container, borderwidth = 5, relief = "ridge")

        nameLabel = ttk.Label(contentFrame, text = "Name")
        nameEntry = ttk.Entry(contentFrame)
        nameEntry.focus_set()

        surnameLabel = ttk.Label(contentFrame, text = "Surname")
        surnameEntry = ttk.Entry(contentFrame)

        fatherNameLabel = ttk.Label(contentFrame, text = "Father's Name")
        fatherNameEntry = ttk.Entry(contentFrame)

        idCardLabel = ttk.Label(contentFrame, text = "Identity Card Number")
        idCardEntry = ttk.Entry(contentFrame)

        athleteCardLabel = ttk.Label(contentFrame, text = "Athlete Card Number")
        athleteCardEntry = ttk.Entry(contentFrame)

        ethnicityLabel = ttk.Label(contentFrame, text = "Ethnicity")
        ethnicitySelectorEntry = AutocompleteEntry(contentFrame)
        ethnicitySelector = AutocompleteCombobox(contentFrame)
        ethnicitySelector.set_completion_list(("Country1", "Country2", "CoutryABCDE", "Country12", "Country4", "CountryEFGHIG"))
        # TODO: CREATE FUNCTION THAN RETURNS ALL COUNTRIES IN A SET
        
        nameLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        nameEntry.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        
        surnameLabel.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        surnameEntry.grid(row = 1, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        fatherNameLabel.grid(row = 0, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        fatherNameEntry.grid(row = 1, column = 4, columnspan = 2, padx = 10, sticky = tk.W)     

        idCardLabel.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        idCardEntry.grid(row = 3, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        athleteCardLabel.grid(row = 2, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        athleteCardEntry.grid(row = 3, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        ethnicityLabel.grid(row = 2, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        ethnicitySelectorEntry.grid(row = 3, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        ethnicitySelector.grid(row = 3, column = 4, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame

    def createBirthdayFrame(self, container):
        contentFrame = ttk.Frame(container, borderwidth = 5, relief = "ridge")

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
 
        ageYear.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        yearSelector.grid(row = 1, column = 0, columnspan = 2, padx=10, sticky = tk.W)

        ageMonth.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        monthSelector.grid(row = 1, column = 2, columnspan = 2, padx=10, sticky = tk.W)

        ageDay.grid(row = 0, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        daySelector.grid(row = 1, column = 4, columnspan = 2, padx=10, sticky = tk.W)

        return contentFrame

    def createContactInfoFrame(self, container):
        contentFrame = ttk.Frame(container, borderwidth = 5, relief = "ridge")

        streetLabel = ttk.Label(contentFrame, text = "Street")
        streetEntry = ttk.Entry(contentFrame)
        
        numberLabel = ttk.Label(contentFrame, text = "Street No.")
        numberEntry = ttk.Entry(contentFrame)

        cityLabel = ttk.Label(contentFrame, text = "City")
        cityEntry = ttk.Entry(contentFrame)

        postCodeLabel = ttk.Label(contentFrame, text = "Post Code")
        postCodeEntry = ttk.Entry(contentFrame)
        
        stateLabel = ttk.Label(contentFrame, text = "State/Province")
        stateEntry = ttk.Entry(contentFrame)

        phoneLabel = ttk.Label(contentFrame, text = "Phone")
        phoneEntry = ttk.Entry(contentFrame)

        emailLabel = ttk.Label(contentFrame, text = "Email")
        emailEntry = ttk.Entry(contentFrame)

        streetLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        streetEntry.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        numberLabel.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        numberEntry.grid(row = 1, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        cityLabel.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        cityEntry.grid(row = 3, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        postCodeLabel.grid(row = 2, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        postCodeEntry.grid(row = 3, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        stateLabel.grid(row = 2, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        stateEntry.grid(row = 3, column = 4, columnspan = 2, padx = 10, sticky = tk.W)

        phoneLabel.grid(row = 4, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        phoneEntry.grid(row = 5, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        emailLabel.grid(row = 4, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        emailEntry.grid(row = 5, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame

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
