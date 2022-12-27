import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame

class StandingsPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        tk.Label(self.scrollable_frame, text="Standings").grid(row=2, column=1)
        contentFrame = self.createTreeview()
        contentFrame.grid(row = 3, column = 0, columnspan = 10, rowspan = 20)
        self.create_standings_table()

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
        self.tree["columns"] = [x for x in range(1,4,1)]
        self.tree["show"] = "headings"
        print("-----" + str(self.tree["columns"]))
        self.tree.column("1", width=100, anchor='c')
        self.tree.column("2", width=100, anchor='c')
        self.tree.column("3", width=100, anchor='c')
        self.tree.heading("1", text="Account")
        self.tree.heading("2", text="Type")
        self.tree.heading("3", text="Dummy")
        self.tree.insert("",'end',text="L1",values=("Big1","Best","D1"))
        self.tree.insert("",'end',text="L2",values=("Big2","Best","D2"))
        self.tree.insert("",'end',text="L3",values=("Big3","Best","D3"))
        self.tree.insert("",'end',text="L4",values=("Big4","Best","D3"))
        self.tree.insert("",'end',text="L5",values=("Big5","Best","D4"))
        self.tree.insert("",'end',text="L6",values=("Big6","Best","D5"))
        self.tree.insert("",'end',text="L7",values=("Big7","Best",""))
        self.tree.insert("",'end',text="L8",values=("Big8","Best",""))
        self.tree.insert("",'end',text="L9",values=("Big9","Best","D89889"))
        self.tree.insert("",'end',text="L10",values=("Big10","Best","D4"))
        self.tree.insert("",'end',text="L11",values=("Big11","Best",""))
        self.tree.insert("",'end',text="L12",values=("Big12","Best","D6"))