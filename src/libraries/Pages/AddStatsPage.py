import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.QuerySelector import QuerySelector

class AddStatsPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)        # STELIOOO CHECKare row column spans etc..
        self.inputs = {}

        tk.Label(self.scrollable_frame, text="Add Statistic").grid(row=1, column=0, sticky = tk.W)
        # ID is assigned automatically

        self.statsInfoFrame = self.createStatsInfoFrame()
        tk.Label(self.scrollable_frame, text = "Stats Info").grid(row = 2, column = 0, sticky = tk.W)
        self.statsInfoFrame.grid(row = 3, column = 0, columnspan = 6, rowspan = 4, sticky = tk.W)

    def onSubmit(self):
        super().onSubmit(self.inputs, 'club')

    def createStatsInfoFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        playerLabel = ttk.Label(contentFrame, text = "Player")
        playerSelector = ttk.Combobox(contentFrame, state = "readonly")
        playerSelector["values"] = QuerySelector.getPlayers()
        self.inputs["player"] = playerSelector
        playerSelector.focus_set()

        matchLabel = ttk.Label(contentFrame, text = "Match")
        matchSelector = ttk.Combobox(contentFrame, state = "readonly")
        matchSelector["values"] = QuerySelector.getMatches()
        self.inputs["match"] = matchSelector

        minuteLabel = ttk.Label(contentFrame, text = "Minute")
        minuteEntry = ttk.Entry(contentFrame)
        self.inputs["minute"] = minuteEntry

        statLabel = ttk.Label(contentFrame, text = "Type")
        statSelector = ttk.Combobox(contentFrame, state = "readonly")
        statSelector["values"] = QuerySelector.getStatsTypes()
        self.inputs["stat_name"] = statSelector


        [widget.grid(row = r, column = col, columnspan = 2, padx = 10, sticky = tk.W) for widget,r,col in 
            zip([playerLabel,playerSelector, matchLabel,matchSelector,
                    minuteLabel,minuteEntry, statLabel,statSelector],
                [0,1, 0,1, 2,3, 2,3],   # rows
                [0,0, 2,2, 0,0, 2,2])   # columns
        ]

        return contentFrame