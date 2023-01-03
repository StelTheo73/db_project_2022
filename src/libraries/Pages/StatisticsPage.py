import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.DbReadyQs import DbReadyQs
from libraries.dbIO.DbQueries import QuerySelector
from libraries.dbIO.StatInfoQueries import StatInfoQueries

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
        typeSelector["values"] = ["Standings", "Player Statistics", "Player Info", "Referee Info", "Match Info"]

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
            try:                
                index = {
                    "team"    : team,
                    "matches" : board[team]["matches"],
                    "points"  : board[team]["points"],
                    "won"     : board[team]["wins"],
                    "drawed"  : board[team]["ties"],
                    "lost"    : board[team]["defeats"],
                    "goals_for" : board[team]["scored_goals"],
                    "goals_against" : board[team]["conceded_goals"],
                    "goal_difference" : board[team]["scored_goals"] - board[team]["conceded_goals"]
                }
            except KeyError as e:
                
                continue

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
        headings = ["Home Team", "Away Team", "Score", "Date",
                "G", "A", "OG",
                "F", "P", 
                "OS", "CK",
                "YC", "RC"
            ]
        self.tree["columns"] = [c for c in range(1, 14, 1)]
        self.tree["show"] = "headings"

        for c in range(1, 14, 1):
            if c == 1 or c == 2:
                self.tree.column(str(c), width = 100, anchor = "c")
            elif c == 3 or c == 4:
                self.tree.column(str(c), width = 70, anchor = "c")
            else:
                self.tree.column(str(c), width = 40, anchor = "c")
            self.tree.heading(str(c), text = headings[c-1])

        # Retrieve stats
        match_stat_dict = StatInfoQueries.get_matches_info()

        # Convert dict to list in order to sort
        match_stat_list = []
        for match_id in match_stat_dict.keys():
            for stat_type in QuerySelector.getStatsTypes():
                if stat_type not in match_stat_dict[match_id].keys():
                    match_stat_dict[match_id][stat_type] = 0
            match_stat_list.append(match_stat_dict[match_id])
        # Sort
        match_stat_list = sorted(match_stat_list, key = lambda d: (d["home_team"], d["away_team"], d["datime"]))
        line = 1
        for match in match_stat_list:
            stat = []
            for stat_type in QuerySelector.getStatsTypes():
                stat.append(match[stat_type])
            self.tree.insert("", "end", text = "L"+str(line),
                values = (
                    match["home_team"],
                    match["away_team"],
                    str(match["home_team_goals"]) + ":" + str(match["away_team_goals"]),
                    match["datime"],
                    stat[0], stat[1], stat[2], # goals, assists, own goals 
                    stat[4], stat[6],          # fouls, penalties
                    stat[7], stat[8],          # offsides, corners
                    stat[9], stat[10]          # yellows, reds
                )
            )

    def create_player_stats_table(self):
        headings = ["Team", "Position", "Player Name",
                "G", "A", "OG",
                "FK", "FC", 
                "PK", "PC", 
                "OS", "CK",
                "YC", "RC"
        ]
        self.tree["columns"] = [c for c in range(1, 15, 1)]
        self.tree["show"] = "headings"

        for c in range(1, 15, 1):
            if c == 1:
                self.tree.column(str(c), width = 100, anchor = "c")
            elif c == 2:
                self.tree.column(str(c), width = 50, anchor = "c")
            elif c == 3:
                self.tree.column(str(c), width = 120, anchor = "c")
            else:
                self.tree.column(str(c), width = 40, anchor = "c")
            self.tree.heading(str(c), text = headings[c-1])

        # Retrieve stats
        player_stat_dict = StatInfoQueries.get_players_stats()

        # Convert dict to list in order to sort
        player_stat_list = []
        for player_id in player_stat_dict.keys():
            for stat_type in QuerySelector.getStatsTypes():
                if stat_type not in player_stat_dict[player_id].keys():
                    player_stat_dict[player_id][stat_type] = 0
            player_stat_list.append(player_stat_dict[player_id])
        # Sort
        player_stat_list = sorted(player_stat_list, key = lambda d: (d["team_name"], d["position"], d["surname"], d["name"]))
        
        line = 1
        for player in player_stat_list:
            stat = []
            for stat_type in QuerySelector.getStatsTypes():
                stat.append(player[stat_type])  
            self.tree.insert("", "end", text = "L"+str(line),
                values = (
                    player["team_name"],
                    player["position"],                    
                    player["surname"] + " " + player["name"],
                    stat[0], stat[1], stat[2],
                    stat[3], stat[4], stat[5],
                    stat[6], stat[7], stat[8],
                    stat[9], stat[10]
                ) 
            )
            line+=1

    def create_player_info_table(self):
        headings = ["Team", "Position", "Player Name", "Nationality", "Player ID", "People ID", "Telephone", "Birthdate"]
        self.tree["columns"] = [c for c in range(1, 9, 1)]
        self.tree["show"] = "headings"

        for c in range(1, 9, 1):
            if c == 1 or c == 5:
                self.tree.column(str(c), width = 100, anchor = "c")
            elif c == 2:
                self.tree.column(str(c), width = 50, anchor = "c")
            elif c == 3:
                self.tree.column(str(c), width = 120, anchor = "c")
            else:
                self.tree.column(str(c), width = 70, anchor = "c")
            self.tree.heading(str(c), text = headings[c-1])

        # Retrieve stats
        player_info = StatInfoQueries.get_players_info()
        # Sort
        player_info = sorted(player_info, key = lambda d:
            (d["team_name"] if d["team_name"] else '~', d["position"], d["surname"], d["name"], d["nationality"], d["birthdate"]))

        line = 1
        for player in player_info:
            self.tree.insert("", "end", text = "L"+str(line),
                values = (
                    player["team_name"],
                    player["position"],
                    player["surname"] + " " + player["name"],
                    player["nationality"],
                    player["player_id"],
                    player["people_id"],
                    player["telephone"],
                    player["birthdate"]
                ) 
            )
            line+=1

    def create_referee_info_table(self):
        headings = ["Type", "Referee Name", "Nationality", "Referee ID", "People ID", "Telephone", "Birthdate"]
        self.tree["columns"] = [c for c in range(1, 8, 1)]
        self.tree["show"] = "headings"

        for c in range(1, 8, 1):
            if c == 2:
                self.tree.column(str(c), width = 120, anchor = "c")
            elif c == 4:
                self.tree.column(str(c), width = 100, anchor = "c")
            else:
                self.tree.column(str(c), width = 70, anchor = "c")
            self.tree.heading(str(c), text = headings[c-1])

        # Retrieve stats
        referee_info = StatInfoQueries.get_referees_info()
        # Sort
        referee_info = sorted(referee_info, key = lambda d: (d["type"], d["surname"], d["name"], d["nationality"], d["birthdate"]))

        line = 1
        for referee in referee_info:
            self.tree.insert("", "end", text = "L"+str(line),
                values = (
                    referee["type"],
                    referee["surname"] + " " + referee["name"],
                    referee["nationality"],
                    referee["player_id"],
                    referee["people_id"],
                    referee["telephone"],
                    referee["birthdate"]
                ) 
            )
            line+=1
            
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
            "Referee Info"       : self.create_referee_info_table,
            "Match Info"         : self.create_matches_table 
        }

        self.contentLabel = ttk.Label(self.scrollable_frame, text = stat_type)
        self.contentLabel.grid(row = 12, column = 0)
        self.contentFrame = self.create_treeview()
        self.contentFrame.grid(row = 13, column = 0, columnspan = 100, rowspan = 20)
        stat_map[stat_type]()
