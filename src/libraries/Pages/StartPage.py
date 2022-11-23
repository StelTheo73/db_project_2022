import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame

class StartPage(MainFrame):
    def __init__(self, master):
        ## Let's make this the page where the user can give his queries
        MainFrame.__init__(self, master)

        #tk.Label(self, text="This is the Start Page").pack(side="top", fill="x", pady=10)
        tk.Label(self.scrollable_frame, text="This is the Start Page").grid(row=1, column=1)

