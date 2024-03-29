import tkinter as tk
import tkinter.ttk as ttk
from libraries.dbIO.DbQueries import DbQueries

class MainFrame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        canvas = tk.Canvas(self, border = 0, highlightthickness = 0)
        self.scrollable_frame = ttk.Frame(canvas)
        self.inputs = {}

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_frame.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Set Scrollbar
        scrollbarX = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)
        scrollbarY = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        
        scrollbarX.pack(fill=tk.X, side = tk.BOTTOM)
        canvas.pack(expand = True, fill = tk.BOTH, side = tk.LEFT)
        scrollbarY.pack(fill = tk.BOTH, side = tk.LEFT)

        canvas["yscrollcommand"] = scrollbarY.set
        canvas["xscrollcommand"] = scrollbarX.set

        # General Page Control Buttons
        self.submitButton = ttk.Button(self.scrollable_frame, text="Submit",
                  command= self.onSubmit, width = 15)

        addPlayerPageButton = ttk.Button(self.scrollable_frame, text="Add Player",
                  command=lambda: master.switchFrame("Add Player"), width = 15)
        addPlayerPageButton.grid(row=0, column=0)
        
        addRefereePageButton = ttk.Button(self.scrollable_frame, text="Add Referee",
                  command=lambda: master.switchFrame("Add Referee"), width = 15)
        addRefereePageButton.grid(row=0, column=1)

        addteamPageButton = ttk.Button(self.scrollable_frame, text="Add Team",
                  command=lambda: master.switchFrame("Add Team"), width = 15)
        addteamPageButton.grid(row=0, column=2)

        addMatchPageButton = ttk.Button(self.scrollable_frame, text="Add Match",
                  command=lambda: master.switchFrame("Add Match"), width = 15)
        addMatchPageButton.grid(row=0, column=3)
        
        addStatisticPageButton = ttk.Button(self.scrollable_frame, text="Add Statistic",
                  command=lambda: master.switchFrame("Add Stat"), width = 15)
        addStatisticPageButton.grid(row=0, column=4)
        
        startPageButton = ttk.Button(self.scrollable_frame, text="Home Page",
                  command=lambda: master.switchFrame("StartPage"), width = 15)
        startPageButton.grid(row=0, column=5)

        deletePlayerPageButton = ttk.Button(self.scrollable_frame, text="Delete Player",
                  command=lambda: master.switchFrame("Delete Player"), width = 15)
        deletePlayerPageButton.grid(row=1, column=0)
        
        deleteRefereePageButton = ttk.Button(self.scrollable_frame, text="Delete Referee",
                  command=lambda: master.switchFrame("Delete Referee"), width = 15)
        deleteRefereePageButton.grid(row=1, column=1)

        deleteTeamPageButton = ttk.Button(self.scrollable_frame, text="Delete Team",
                  command=lambda: master.switchFrame("Delete Team"), width = 15)
        deleteTeamPageButton.grid(row=1, column=2)

        deleteMatchPageButton = ttk.Button(self.scrollable_frame, text="Delete Match",
                  command=lambda: master.switchFrame("Delete Match"), width = 15)
        deleteMatchPageButton.grid(row=1, column=3)
        
        deleteStatisticPageButton = ttk.Button(self.scrollable_frame, text="Delete Statistic",
                  command=lambda: master.switchFrame("Delete Stat"), width = 15)
        deleteStatisticPageButton.grid(row=1, column=4)
        
        standingsPageButton = ttk.Button(self.scrollable_frame, text="Statistics",
                  command=lambda: master.switchFrame("Statistics"), width = 15)
        standingsPageButton.grid(row=1, column=5)

    def onSubmit(self, method=''):
        methods = {
            ''       : None,
            'player' : DbQueries.insert_player,
            'referee': DbQueries.insert_referee,
            'team'   : DbQueries.insert_team,
            'match'  : DbQueries.insert_match,
            'stat'   : DbQueries.insert_stat,
            'delete_player'  : DbQueries.delete_player,
            'delete_referee' : DbQueries.delete_referee,
            'delete_team'    : DbQueries.delete_team,
            'delete_match'   : DbQueries.delete_match,
            'delete_stat'    : DbQueries.delete_stat,
            'query': DbQueries.run_query
        }
        DbQueries.submit(self.inputs, methods[method])

