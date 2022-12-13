import tkinter as tk
import tkinter.ttk as ttk
from libraries.dbIO.DbQueries import DbQueries

class MainFrame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        canvas = tk.Canvas(self)
        scrollbarY = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbarY.pack(side="right", fill="y")
        canvas["yscrollcommand"] = scrollbarY.set

        addPlayerPageButton = ttk.Button(self.scrollable_frame, text="Add Player",
                  command=lambda: master.switchFrame("Add Player"))
        addPlayerPageButton.grid(row=0, column=0)
        
        addRefereePageButton = ttk.Button(self.scrollable_frame, text="Add Referee",
                  command=lambda: master.switchFrame("Add Referee"))
        addRefereePageButton.grid(row=0, column=1)

        addteamPageButton = ttk.Button(self.scrollable_frame, text="Add Team",
                  command=lambda: master.switchFrame("Add Team"))
        addteamPageButton.grid(row=0, column=2)

        addMatchPageButton = ttk.Button(self.scrollable_frame, text="Add Match",
                  command=lambda: master.switchFrame("Add Match"))
        addMatchPageButton.grid(row=0, column=3)
        
        addStatisticPageButton = ttk.Button(self.scrollable_frame, text="Add Statistic",
                  command=lambda: master.switchFrame("Add Stat"))
        addStatisticPageButton.grid(row=0, column=4)
        
        startPageButton = ttk.Button(self.scrollable_frame, text="Open start page",
                  command=lambda: master.switchFrame("StartPage"))
        startPageButton.grid(row=0, column=5)
        
        submitButton = ttk.Button(self.scrollable_frame, text="Submit",
                  command= self.onSubmit, width=40, padding=5)
        submitButton.grid(row=100, column=1, columnspan=2)
    
    def onSubmit(self, entries={}, method=''):
        methods = {'':None,
            'player': DbQueries.update_players,
            'referee': DbQueries.update_referees,
            'club': DbQueries.update_clubs,
            'match': DbQueries.update_matches,
            'stat': DbQueries.update_stats,
            'query': DbQueries.run_query,
        }
        DbQueries.submit(entries, methods[method])

