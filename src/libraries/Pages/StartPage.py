import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import askyesno, askokcancel
from libraries.MainFrame import MainFrame
from libraries.dbIO.DbQueries import QuerySelector
from generators.init import initialize, flush

class StartPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)

        tk.Label(self.scrollable_frame, text="Custom Query").grid(row=2, column=0)
        self.createQueryFrame().grid(row = 3, column = 0, columnspan = 8, rowspan = 1, sticky = tk.W)

        self.submitButton.destroy()
        self.submitQueryButton = ttk.Button(self.scrollable_frame, text="Submit",
            command= self.onSubmit, width = 15)
        self.submitQueryButton.grid(row = 4, column = 0, pady = 10, sticky = tk.W)
        
        self.createInitFrame().grid(row = 5, column = 0, pady = 10, rowspan = 4, columnspan = 8, sticky = tk.W)

        self.initButton = ttk.Button(self.scrollable_frame, text = "Initialize DB", command = self.initializeDB, width = 15)
        self.initButton.grid(row = 9, column = 0, pady = 10, columnspan = 2, sticky = tk.W)
        self.initButton.bind("<Return>", lambda e: self.initializeDB())

        self.flushButton = ttk.Button(self.scrollable_frame, text = "Flush BD", command = self.flushDB, width = 15)
        self.flushButton.grid(row = 9, column = 1, pady = 10, columnspan = 2, sticky = tk.W)
        self.flushButton.bind("<Return>", lambda e: self.flushDB())

    def onSubmit(self):
        super().onSubmit('query')

    def initializeDB(self):
        teams = {func: self.inputs[func].get() for func in self.inputs}["teams"]
        players = {func: self.inputs[func].get() for func in self.inputs}["players"]
        referees = {func: self.inputs[func].get() for func in self.inputs}["referees"]
        season = {func: self.inputs[func].get() for func in self.inputs}["season"]
        if teams and season and players and referees:
            userAction = askyesno(title = "Warning!", message = "This action will overwrite the data of the database.\nDo you wish to proceed?")
            if userAction == 1: # Answered OK
                initialize(int(players), int(referees), int(teams), int(season))
        else:
            askokcancel(title = "Incomplete input!", message = "Please provide information for teams, season, players and referees.")

    def flushDB(self):
        userAction = askyesno(title = "Warning!", message = "This action will permanently delete all data from the database.\nDo you wish to proceed?")
        print(userAction)
        if userAction:
            flush()

    def createQueryFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth=5, relief="ridge")
        
        queryLabel = ttk.Label(contentFrame, text = "Query")
        
        queryEntry = ttk.Entry(contentFrame, width=110,\
            validate='key', validatecommand=(contentFrame.register(lambda txt: txt[:7]=='SELECT '), '%P'))
        queryEntry.insert(0, 'SELECT ')
        self.inputs['query'] = queryEntry
        queryEntry.focus_set()

        
        queryLabel.grid(row = 0, column = 0, columnspan = 1, padx = 10, sticky = tk.W)
        queryEntry.grid(row = 1, column = 0, columnspan = 1, padx = 10, sticky = tk.W)

        return contentFrame

    def createInitFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        teamLabel = ttk.Label(contentFrame, text = "No. of teams")
        teamSelector = ttk.Combobox(contentFrame, state = "readonly", width = 30)
        teamSelector["values"] = [x for x in range(2, 30, 2)]
        self.inputs["teams"] = teamSelector

        seasonLabel = ttk.Label(contentFrame, text = "Season")
        seasonSelector = ttk.Combobox(contentFrame, state = "readonly", width = 30)
        seasonSelector["values"] = QuerySelector.getLastYears()
        self.inputs["season"] = seasonSelector
        
        playerLabel = ttk.Label(contentFrame, text = "No. of players")
        playerSelector = ttk.Combobox(contentFrame, state = "readonly", width = 30)
        playerSelector["values"] = [x for x in range(100, 2100, 100)]
        self.inputs["players"] = playerSelector

        refereeLabel = ttk.Label(contentFrame, text = "No. of referees")
        refereeSelector = ttk.Combobox(contentFrame, state = "readonly", width = 30)
        refereeSelector["values"] = [x for x in range(100, 1050, 50)]
        self.inputs["referees"] = refereeSelector

        teamLabel.grid(row = 0, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        teamSelector.grid(row = 1, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        seasonLabel.grid(row = 0, column = 4, columnspan = 4, padx = 10, sticky = tk.W)
        seasonSelector.grid(row = 1, column = 4, columnspan = 4, padx = 10, sticky = tk.W)
        playerLabel.grid(row = 2, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        playerSelector.grid(row = 3, column = 0, columnspan = 4, padx = 10, sticky = tk.W)
        refereeLabel.grid(row = 2, column = 4, columnspan = 4, padx = 10, sticky = tk.W)
        refereeSelector.grid(row = 3, column = 4, columnspan = 4, padx = 10, sticky = tk.W)

        return contentFrame