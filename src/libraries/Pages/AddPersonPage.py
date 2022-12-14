import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.QuerySelector import QuerySelector

class AddPersonPage(MainFrame):
    def __init__(self, master, personType:str):
        MainFrame.__init__(self, master)
        self.personType, self.inputs = personType, {}
        tk.Label(self.scrollable_frame, text="Add "+self.personType).grid(row=1, column=0, sticky = tk.W)
        
        tk.Label(self.scrollable_frame, text = "Personal Info").grid(row = 2, column = 0, sticky = tk.W)
        self.createPersonalInfoFrame().grid(row = 3, column = 0, columnspan = 8, rowspan = 4, sticky = tk.W)
        
        tk.Label(self.scrollable_frame, text = "Birthday").grid(row = 7, column = 0, sticky = tk.W)
        self.createBirthdayFrame().grid(row = 8, column = 0, columnspan = 6, rowspan = 2, sticky = tk.W)

        tk.Label(self.scrollable_frame, text = "Contact Info").grid(row = 10, column = 0, sticky = tk.W)
        self.createContactInfoFrame().grid(row = 11, column = 0, columnspan = 6, rowspan = 6, sticky = tk.W)

    def onSubmit(self):
        super().onSubmit(self.inputs, self.personType.lower())

    def createPersonalInfoFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        nameLabel = ttk.Label(contentFrame, text = "Name")
        nameEntry = ttk.Entry(contentFrame)
        self.inputs["name"] = nameEntry
        nameEntry.focus_set()

        surnameLabel = ttk.Label(contentFrame, text = "Surname")
        surnameEntry = ttk.Entry(contentFrame)
        self.inputs["surname"] = surnameEntry

        idLabel = ttk.Label(contentFrame, text = "Identity Card Number")
        idEntry = ttk.Entry(contentFrame)
        self.inputs["id"] = idEntry

        athleteCardLabel = ttk.Label(contentFrame, text = self.personType+" Card Number")
        athleteCardEntry = ttk.Entry(contentFrame)
        self.inputs["card"] = athleteCardEntry

        nationalityLabel = ttk.Label(contentFrame, text = "Nationality")
        nationalitySelector = ttk.Combobox(contentFrame, state = "readonly")
        nationalitySelector["values"] = QuerySelector.getCountries()
        self.inputs["nationality"] = nationalitySelector

        nameLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        nameEntry.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        
        surnameLabel.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        surnameEntry.grid(row = 1, column = 2, columnspan = 2, padx = 10, sticky = tk.W)  

        idLabel.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        idEntry.grid(row = 3, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        athleteCardLabel.grid(row = 2, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        athleteCardEntry.grid(row = 3, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        nationalityLabel.grid(row = 2, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        nationalitySelector.grid(row = 3, column = 4, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame

    def createBirthdayFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        ageYear = ttk.Label(contentFrame, text = "Year")
        yearSelector = ttk.Combobox(contentFrame, state = "readonly")
        yearSelector["values"] = QuerySelector.getLastYears(max_age=65, min_age=15)
        self.inputs["year"] = yearSelector
        
        ageMonth = ttk.Label(contentFrame, text = "Month")
        monthSelector = ttk.Combobox(contentFrame, state = "readonly")
        monthSelector["values"] = [str(month).zfill(2) for month in range(1, 13)]
        self.inputs["month"] = monthSelector

        ageDay = ttk.Label(contentFrame, text = "Day")
        daySelector = ttk.Combobox(contentFrame, state = "readonly")
        daySelector["values"] = [str(day).zfill(2) for day in range(1, 32)]
        self.inputs["day"] = daySelector
 
        ageYear.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        yearSelector.grid(row = 1, column = 0, columnspan = 2, padx=10, sticky = tk.W)

        ageMonth.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        monthSelector.grid(row = 1, column = 2, columnspan = 2, padx=10, sticky = tk.W)

        ageDay.grid(row = 0, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        daySelector.grid(row = 1, column = 4, columnspan = 2, padx=10, sticky = tk.W)

        return contentFrame

    def createContactInfoFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")
        phoneLabel = ttk.Label(contentFrame, text = "Phone")
        phoneEntry = ttk.Entry(contentFrame)
        self.inputs["tel"] = phoneEntry

        phoneLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        phoneEntry.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame