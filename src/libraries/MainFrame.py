import tkinter as tk
import tkinter.ttk as ttk
from libraries.dbIO.QuerySelector import QuerySelector as Queries

class MainFrame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        canvas = tk.Canvas(self)
        scrollbarY = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.pack(side="left", fill="both", expand=True)
        scrollbarY.pack(side="right", fill="y")
        canvas["yscrollcommand"] = scrollbarY.set

        pageOneButton = ttk.Button(self.scrollable_frame, text="Add Player",
                  command=lambda: master.switchFrame("Add Player"))
        pageOneButton.grid(row=0, column=0)
        
        pageTwoButton = ttk.Button(self.scrollable_frame, text="Add Referee",
                  command=lambda: master.switchFrame("Add Referee"))
        pageTwoButton.grid(row=0, column=1)

        pageThreeButton = ttk.Button(self.scrollable_frame, text="Add Team",
                  command=lambda: master.switchFrame("Add Team"))
        pageThreeButton.grid(row=0, column=2)

        startPageButton = ttk.Button(self.scrollable_frame, text="Add Match",
                  command=lambda: master.switchFrame("Add Match"))
        startPageButton.grid(row=0, column=3)
        
        startPageButton = ttk.Button(self.scrollable_frame, text="Open start page",
                  command=lambda: master.switchFrame("StartPage"))
        startPageButton.grid(row=0, column=4)
        
        startPageButton = ttk.Button(self.scrollable_frame, text="Submit",
                  command= self.onSubmit, width=40, padding=5)
        startPageButton.grid(row=100, column=1, columnspan=2)
    
    def onSubmit(self, entries={}, method=''):
        methods = {'':None,
            'player': Queries.update_players,
            'referee': Queries.update_referees,
            'club': Queries.update_clubs,
            'match': Queries.update_matches,
            'stat': Queries.update_stats,
            'query': Queries.run_query,
        }
        Queries.submit(entries, methods[method])

