import tkinter as tk
import tkinter.ttk as ttk
# from libraries.Autocomplete.AutocompleteEntry import AutocompleteCombobox, AutocompleteEntry
from libraries.MainFrame import MainFrame

class AddPersonPage(MainFrame):
    def __init__(self, master, personType=""):
        MainFrame.__init__(self, master)

        self.personType = personType
        self.inputs = {}

        self.personalInfoFrame = self.createPersonalInfoFrame(self.scrollable_frame)
        self.birthdayFrame = self.createBirthdayFrame(self.scrollable_frame)
        self.contactInfoFrame =  self.createContactInfoFrame(self.scrollable_frame)
        
        tk.Label(self.scrollable_frame, text = "Personal Info").grid(row = 2, column = 0, sticky = tk.W)
        self.personalInfoFrame.grid(row = 3, column = 0, columnspan = 8, rowspan = 4, sticky = tk.W)
        
        tk.Label(self.scrollable_frame, text = "Birthday").grid(row = 7, column = 0, sticky = tk.W)
        self.birthdayFrame.grid(row = 8, column = 0, columnspan = 6, rowspan = 2, sticky = tk.W)
    #   DATE PICKER FOR TKINTER: https://www.geeksforgeeks.org/create-a-date-picker-calendar-tkinter/

        tk.Label(self.scrollable_frame, text = "Contact Info").grid(row = 10, column = 0, sticky = tk.W)
        self.contactInfoFrame.grid(row = 11, column = 0, columnspan = 6, rowspan = 6, sticky = tk.W)

    def onSubmit(self):
        super().onSubmit(self.inputs, self.personType)

    def createPersonalInfoFrame(self, container):
        contentFrame = ttk.Frame(container, borderwidth = 5, relief = "ridge")

        nameLabel = ttk.Label(contentFrame, text = "Name")
        nameEntry = ttk.Entry(contentFrame)
        self.inputs["name"] = nameEntry
        # nameEntry.focus_set()

        surnameLabel = ttk.Label(contentFrame, text = "Surname")
        surnameEntry = ttk.Entry(contentFrame)
        self.inputs["surname"] = surnameEntry

        idLabel = ttk.Label(contentFrame, text = "Identity Card Number")
        idEntry = ttk.Entry(contentFrame)
        self.inputs["id"] = idEntry

        athleteCardLabel = ttk.Label(contentFrame, text = self.personType+" Card Number")
        athleteCardEntry = ttk.Entry(contentFrame)
        self.inputs["card"] = athleteCardEntry

        ethnicityLabel = ttk.Label(contentFrame, text = "Nationality")
        ethnicitySelector = ttk.Combobox(contentFrame, state = "readonly")
        ethnicitySelector["values"] = ["Greece", "Country2", "Coutry3", "Country4", "Country5", "Country6"]
        # TODO: CREATE FUNCTION THAN RETURNS ALL COUNTRIES
        self.inputs["nationality"] = ethnicitySelector

        
        nameLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        nameEntry.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        
        surnameLabel.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        surnameEntry.grid(row = 1, column = 2, columnspan = 2, padx = 10, sticky = tk.W)  

        idLabel.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        idEntry.grid(row = 3, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        athleteCardLabel.grid(row = 2, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        athleteCardEntry.grid(row = 3, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        ethnicityLabel.grid(row = 2, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        ethnicitySelector.grid(row = 3, column = 4, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame

    def createBirthdayFrame(self, container):
        contentFrame = ttk.Frame(container, borderwidth = 5, relief = "ridge")

        ageYear = ttk.Label(contentFrame, text = "Year")
        selectedYear = tk.IntVar()
        yearSelector = ttk.Combobox(contentFrame, textvariable = selectedYear, state = "readonly")
        yearSelector["values"] = [year for year in range(1970, 2008, 1)]
        # TODO : CREATE FUNTCION THAT RETURNS ALL YEARS FROM 1970 TILL CURRENT_YEAR - 15
        self.inputs["year"] = yearSelector
        
        
        ageMonth = ttk.Label(contentFrame, text = "Month")
        selectedMonth = tk.StringVar()
        monthSelector = ttk.Combobox(contentFrame, textvariable = selectedMonth, state = "readonly")
        monthSelector["values"] = [month for month in ["JAN", "FEB", "MAR", "APR", "JUN", 
                                                            "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]]
        # TODO : CREATE FUNTCION THAT RETURNS ALL MONTHS
        self.inputs["month"] = monthSelector

        ageDay = ttk.Label(contentFrame, text = "Day")
        selectedDay = tk.IntVar()
        daySelector = ttk.Combobox(contentFrame, textvariable = selectedDay, state = "readonly")
        daySelector["values"] = [day for day in range(1, 32, 1)]
        # TODO : CREATE FUNTCION THAT RETURNS DAYS OF SELECTED MONTH
        self.inputs["day"] = daySelector
 
        ageYear.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        yearSelector.grid(row = 1, column = 0, columnspan = 2, padx=10, sticky = tk.W)

        ageMonth.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        monthSelector.grid(row = 1, column = 2, columnspan = 2, padx=10, sticky = tk.W)

        ageDay.grid(row = 0, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        daySelector.grid(row = 1, column = 4, columnspan = 2, padx=10, sticky = tk.W)

        return contentFrame

    def createContactInfoFrame(self, container):
        contentFrame = ttk.Frame(container, borderwidth = 5, relief = "ridge")
        phoneLabel = ttk.Label(contentFrame, text = "Phone")
        phoneEntry = ttk.Entry(contentFrame)
        self.inputs["phone"] = phoneEntry

        emailLabel = ttk.Label(contentFrame, text = "Email")
        emailEntry = ttk.Entry(contentFrame)
        self.inputs["email"] = emailEntry

        phoneLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        phoneEntry.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        emailLabel.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        emailEntry.grid(row = 1, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame