import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame

class StartPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        #tk.Label(self, text="This is the Start Page").pack(side="top", fill="x", pady=10)
        tk.Label(self, text="This is the Start Page").grid(row=1, column=1)
