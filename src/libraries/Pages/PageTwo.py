import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame

class PageTwo(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        tk.Label(self.scrollable_frame, text="This is page two").grid(row=1, column=1)



    def createTreeview(self):
        print("created")
        self.tree = ttk.self.Treeview(self, selectmode="browse")
        self.tree.grid(row=2, column=0, columnspan=1)
        self.tree_vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        self.tree_vsb.pack(side="right", fill="y")
        self.tree_hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree_hsb.pack(side="bottom", fill="x")
        self.tree.configure(yscrollcommand=self.tree_vsb.set)
        self.tree.configure(xscrollcommand=self.tree_hsb.set)

        self.tree["columns"] = ("1", "2")
        self.tree["show"] = "headings"

        self.tree.column("1", width=100, anchor='c')
        self.tree.column("2", width=100, anchor='c')
        self.tree.heading("1", text="Account")
        self.tree.heading("2", text="Type")
        self.tree.insert("",'end',text="L1",values=("Big1","Best"))
        self.tree.insert("",'end',text="L2",values=("Big2","Best"))
        self.tree.insert("",'end',text="L3",values=("Big3","Best"))
        self.tree.insert("",'end',text="L4",values=("Big4","Best"))
        self.tree.insert("",'end',text="L5",values=("Big5","Best"))
        self.tree.insert("",'end',text="L6",values=("Big6","Best"))
        self.tree.insert("",'end',text="L7",values=("Big7","Best"))
        self.tree.insert("",'end',text="L8",values=("Big8","Best"))
        self.tree.insert("",'end',text="L9",values=("Big9","Best"))
        self.tree.insert("",'end',text="L10",values=("Big10","Best"))
        self.tree.insert("",'end',text="L11",values=("Big11","Best"))
        self.tree.insert("",'end',text="L12",values=("Big12","Best"))