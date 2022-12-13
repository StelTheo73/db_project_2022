import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.QuerySelector import QuerySelector

class AddMatchPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)        # STELIOOO CHECKare row column spans etc..
        self.inputs = {}

        tk.Label(self.scrollable_frame, text="Add match").grid(row=1, column=0, sticky = tk.W)
        # ID is assigned automatically

        tk.Label(self.scrollable_frame, text = "Match Datetime").grid(row = 2, column = 0, sticky = tk.W)
        self.createMatchDateFrame().grid(row = 3, column = 0, columnspan = 6, rowspan = 2, sticky = tk.W)

        tk.Label(self.scrollable_frame, text = "Match Score").grid(row = 5, column = 0, sticky = tk.W)
        self.createMatchScoreFrame().grid(row = 6, column = 0, columnspan = 6, rowspan = 2, sticky = tk.W)

        tk.Label(self.scrollable_frame, text="Referees that control the match").grid(row = 8, column = 0, sticky = tk.W)
        self.createRefereesFrame().grid(row = 9, column = 0, columnspan = 8, rowspan = 2, sticky = tk.W)

    def onSubmit(self):
        super().onSubmit(self.inputs, 'match')

    def createMatchDateFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        yearLabel = ttk.Label(contentFrame, text = "Year")
        yearSelector = ttk.Combobox(contentFrame, state="readonly")
        yearSelector["values"] = QuerySelector.getLastYears() #[year for year in range(2000, 2024)]
        self.inputs["year"] = yearSelector

        monthLabel = ttk.Label(contentFrame, text = "Month")
        monthSelector = ttk.Combobox(contentFrame, state="readonly")
        monthSelector["values"] = [str(month).zfill(2) for month in range(1, 13)]
        self.inputs["month"] = monthSelector

        dayLabel = ttk.Label(contentFrame, text = "Day")
        daySelector = ttk.Combobox(contentFrame, state="readonly")
        daySelector["values"] = [str(day).zfill(2) for day in range(1, 32)]
        self.inputs["day"] = daySelector

        hourLabel = ttk.Label(contentFrame, text = "Hour")
        hourSelector = ttk.Combobox(contentFrame, state="readonly")
        hourSelector["values"] = [str(hour).zfill(2) for hour in range(0, 24)]
        self.inputs["hour"] = hourSelector

        minuteLabel = ttk.Label(contentFrame, text = "Minute")
        minuteSelector = ttk.Combobox(contentFrame, state="readonly")
        minuteSelector["values"] = [str(min).zfill(2) for min in range(0, 60, 15)]
        self.inputs["minute"] = minuteSelector


        [widget.grid(row = r, column = col, columnspan = 2, padx = 10, sticky = tk.W) for widget,r,col in 
            zip([yearLabel,yearSelector, monthLabel,monthSelector, dayLabel,daySelector,
                    hourLabel,hourSelector, minuteLabel,minuteSelector],
                [0,1, 0,1, 0,1, 2,3, 2,3],   # rows
                [0,0, 2,2, 4,4, 1,1, 3,3])   # columns
        ]
        
        return contentFrame

    def createMatchScoreFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")
        
        homeTeamLabel = ttk.Label(contentFrame, text = "Home team")
        homeTeamEntry = ttk.Combobox(contentFrame, state="readonly")
        homeTeamEntry["values"] = QuerySelector.getTeams()
        self.inputs["home_team"] = homeTeamEntry
        
        awayTeamLabel = ttk.Label(contentFrame, text = "Away team")
        awayTeamEntry = ttk.Combobox(contentFrame, state="readonly")
        awayTeamEntry["values"] = QuerySelector.getTeams()
        self.inputs["away_team"] = awayTeamEntry

        homeScoreLabel = ttk.Label(contentFrame, text = "Home team score")
        homeScoreEntry = ttk.Combobox(contentFrame, state="readonly")
        homeScoreEntry["values"] = [goals for goals in range(0, 50)]
        self.inputs["home_score"] = homeScoreEntry

        awayScoreLabel = ttk.Label(contentFrame, text = "Away team score")
        awayScoreEntry = ttk.Combobox(contentFrame, state="readonly")
        awayScoreEntry["values"] = [goals for goals in range(0, 50)]
        self.inputs["away_score"] = awayScoreEntry
        
        
        [widget.grid(row = r, column = col, columnspan = 2, padx = 10, sticky = tk.W) for widget,r,col in 
            zip([homeTeamLabel,homeTeamEntry, awayTeamLabel,awayTeamEntry,
                    homeScoreLabel,homeScoreEntry, awayScoreLabel,awayScoreEntry],
                [0,1, 0,1, 2,3, 2,3],   # rows
                [1,1, 3,3, 1,1, 3,3])   # columns
        ]

        return contentFrame

    def createRefereesFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")
        
        headRefereeLabel = ttk.Label(contentFrame, text = "Head Referee")
        headRefereeEntry = ttk.Combobox(contentFrame, state="readonly")
        headRefereeEntry["values"] = QuerySelector.getRefereesByType("Head")
        self.inputs["head_ref"] = headRefereeEntry
        
        firstAssistantLabel = ttk.Label(contentFrame, text = "Assistant referee #1")
        firstAssistantEntry = ttk.Combobox(contentFrame, state="readonly")
        firstAssistantEntry["values"] = QuerySelector.getRefereesByType("Assistant")
        self.inputs["assist_ref_1"] = firstAssistantEntry
        
        secondAssistantLabel = ttk.Label(contentFrame, text = "Assistant referee #2")
        secondAssistantEntry = ttk.Combobox(contentFrame, state="readonly")
        secondAssistantEntry["values"] = QuerySelector.getRefereesByType("Assistant")
        self.inputs["assist_ref_2"] = secondAssistantEntry
        
        fourthRefLabel = ttk.Label(contentFrame, text = "Fourth referee")
        fourthRefEntry = ttk.Combobox(contentFrame, state="readonly")
        fourthRefEntry["values"] = QuerySelector.getRefereesByType("Fourth")
        self.inputs["fourth_ref"] = fourthRefEntry

        
        [widget.grid(row = r, column = col, columnspan = 2, padx = 10, sticky = tk.W) for widget,r,col in 
            zip([headRefereeLabel, headRefereeEntry, firstAssistantLabel,firstAssistantEntry,
                    secondAssistantLabel, secondAssistantEntry, fourthRefLabel, fourthRefEntry],
                [0,1]*4,   # rows
                [0,0, 2,2, 4,4, 6,6])   # columns
        ]

        return contentFrame


