import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.DbReadyQs import DbReadyQs

class StatisticsPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        tk.Label(self.scrollable_frame, text="Standings").grid(row=2, column=1)
        contentFrame = self.createTreeview()
        contentFrame.grid(row = 3, column = 0, columnspan = 10, rowspan = 20)
        self.create_standings_table()

    def type_selector(self):
        """Select the type of the statistics to show"""
        pass

    def createTreeview(self):
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
        print(board)
        sorted_board = []
        for team in board:
            matches = board[team]["matches"]
            try: #no wins
                won = board[team]["wins"]
            except KeyError:
                won = 0
                matches+=1
            try: #no defeats
                lost = board[team]["defeats"]
            except KeyError:
                lost = 0
                matches+=1
            try:
                points = board[team]["points"]
            except KeyError: #only ties
                print("\n\n{}".format(board[team]["ties"]))
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

    def create_referee_stats_table(self):
        pass
