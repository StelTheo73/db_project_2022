import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.DbQueries import QuerySelector


class AddMatchPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        tk.Label(self.scrollable_frame, text = "Date & Time").grid(row = 2, column = 0, sticky = tk.W)
        self.match_frame = self.create_match_date_frame().grid(row = 3, column = 0, columnspan = 6, rowspan = 4, sticky = tk.W)
        tk.Label(self.scrollable_frame, text = "Match Info").grid(row = 7, column = 0, sticky = tk.W)
        self.create_match_info_frame().grid(row = 8, column = 0, rowspan = 4, columnspan = 6, sticky = tk.W)
        tk.Label(self.scrollable_frame, text = "Referees").grid(row = 12, column = 0, sticky = tk.W)
        self.create_referees_frame().grid(row = 13, column = 0, rowspan = 4, columnspan = 6, sticky = tk.W)

        self.submitButton.grid(row = 17, column = 0)

    def onSubmit(self):
        super().onSubmit('match')

    def create_match_date_frame(self):
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
        minuteSelector["values"] = [str(minute).zfill(2) for minute in range(0, 60)]
        self.inputs["minute"] = minuteSelector

        yearLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        yearSelector.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        monthLabel.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        monthSelector.grid(row = 1, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        dayLabel.grid(row = 0, column = 4, columnspan = 2, padx = 10, sticky = tk.W)
        daySelector.grid(row = 1, column = 4, columnspan = 2, padx = 10, sticky = tk.W)

        hourLabel.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        hourSelector.grid(row = 3, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        minuteLabel.grid(row = 2, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        minuteSelector.grid(row = 3, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame

    def create_match_info_frame(self):
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

        homeTeamLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        homeTeamEntry.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        awayTeamLabel.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        awayTeamEntry.grid(row = 1, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        homeScoreLabel.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        homeScoreEntry.grid(row = 3, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        awayScoreLabel.grid(row = 2, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        awayScoreEntry.grid(row = 3, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame

    def create_referees_frame(self):
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

        headRefereeLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        headRefereeEntry.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        firstAssistantLabel.grid(row = 0, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        firstAssistantEntry.grid(row = 1, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        secondAssistantLabel.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        secondAssistantEntry.grid(row = 3, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        fourthRefLabel.grid(row = 2, column = 2, columnspan = 2, padx = 10, sticky = tk.W)
        fourthRefEntry.grid(row = 3, column = 2, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame
        