import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.DbReadyQs import DbReadyQs

class StatisticsPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        self.contentLabel = None
        self.contentFrame = None
        self.create_type_selector_frame().grid(row = 2, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)

    def create_type_selector_frame(self):
        """Select the type of the statistics to show"""
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")
        typeLabel = tk.Label(contentFrame, text="Select: ")
        typeSelector = ttk.Combobox(contentFrame, state = "readonly", width = 20)
        typeSelector["values"] = ["Standings", "Player Statistics", "Player Info", "Referee Statistics", "Referee Info", "Match Info"]

        typeSelector.focus_set()
        self.inputs["type"] = typeSelector

        typeSelectorButton = ttk.Button(contentFrame, text = "Select",
                        command= self.select_type)

        typeLabel.grid(row = 0, column = 0, columnspan = 6, padx = 10, sticky = tk.W)
        typeSelector.grid(row = 1, column = 0, columnspan = 6, padx = 10, sticky = tk.W)
        typeSelectorButton.grid(row = 2, column = 0, columnspan = 6, padx = 10, sticky = tk.W)

        return contentFrame

    def create_treeview(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")
        self.tree = ttk.Treeview(contentFrame, selectmode="browse")
        self.tree_vsb = ttk.Scrollbar(contentFrame, orient="vertical", command=self.tree.yview)
        self.tree_hsb = ttk.Scrollbar(contentFrame, orient="horizontal", command=self.tree.xview)        
        
        self.tree_hsb.pack(fill=tk.X, side = tk.BOTTOM)
        self.tree.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.tree_vsb.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        self.tree.configure(yscrollcommand=self.tree_vsb.set)
        self.tree.configure(xscrollcommand=self.tree_hsb.set)

        return contentFrame

    def create_standings_table(self):
        headings = ["Place", "Team", "Matches", "Points", "W", "D", "L", "GF:GA", "+/-"]
        self.tree["columns"] = [c for c in range(1,10,1)]
        self.tree["show"] = "headings"

        for c in range(1, 10, 1):
            if c == 2:
                self.tree.column(str(c), width = 100, anchor = "c")
            elif c == 3:
                self.tree.column(str(c), width = 55, anchor = "c")
            else:
                self.tree.column(str(c), width = 50, anchor = "c")
            self.tree.heading(str(c), text = headings[c-1])
        
        board = DbReadyQs.get_board()
        #print(board)
        sorted_board = []
        for team in board:
            matches = board[team]["matches"]
            try:
                won = board[team]["wins"]
            except KeyError: #no wins
                won = 0
                matches+=1
            try:
                lost = board[team]["defeats"]
            except KeyError: #no defeats
                lost = 0
                matches+=1
            try:
                points = board[team]["points"]
            except KeyError: #only ties
                #print("\n\n{}".format(board[team]["ties"]))
                points = board[team]["ties"]
            index = {
                "team"    : team,
                "matches" : matches,
                "points"  : points,
                "won"     : won,
                "drawed"  : board[team]["ties"],
                "lost"    : lost,
                "goals_for" : board[team]["scored_goals"],
                "goals_against" : board[team]["conceded_goals"],
                "goal_difference" : board[team]["scored_goals"] - board[team]["conceded_goals"]
            }

            sorted_board.append(index)

        sorted_board = sorted(sorted_board, key = lambda d: (d["points"], -d["matches"], d["won"], d["goal_difference"], d["goals_for"], -d["goals_against"]), reverse = True)

        place = 1
        for index in sorted_board:
            self.tree.insert("", "end", text = "L"+str(place),
                values = (place, 
                        index["team"],
                        index["matches"],
                        index["points"],
                        index["won"],
                        index["drawed"],
                        index["lost"],
                        str(index["goals_for"])+":"+str(index["goals_against"]),
                        index["goal_difference"])
            )            
            place+=1

    def create_matches_table(self):
        pass

    def create_player_stats_table(self):
        pass

    def create_player_info_table(self):
        pass

    def create_referee_stats_table(self):
        pass

    def create_referee_info_table(self):
        pass

    def select_type(self):
        stat_type = {func: self.inputs[func].get() for func in self.inputs}["type"]
        if stat_type == "":
            return
        if self.contentLabel != None:
            self.contentLabel.destroy()
        if self.contentFrame != None:
            self.contentFrame.destroy()

        stat_map = {
            "Standings"          : self.create_standings_table,
            "Player Statistics"  : self.create_player_stats_table,
            "Player Info"        : self.create_player_info_table,
            "Referee Statistics" : self.create_referee_stats_table,
            "Referee Info"       : self.create_referee_info_table,
            "Match Info"         : self.create_matches_table 
        }

        self.contentLabel = ttk.Label(self.scrollable_frame, text = stat_type)
        self.contentLabel.grid(row = 12, column = 0)
        self.contentFrame = self.create_treeview()
        self.contentFrame.grid(row = 13, column = 0, columnspan = 10, rowspan = 20)
        stat_map[stat_type]()
