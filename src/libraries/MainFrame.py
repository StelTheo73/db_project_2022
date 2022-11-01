import tkinter as tk
import tkinter.ttk as ttk

class MainFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        pageOneButton = ttk.Button(self, text="Add Player",
                  command=lambda: master.switchFrame("Add Player"))
        pageOneButton.grid(row=0, column=0)
        
        pageTwoButton = ttk.Button(self, text="Open page two",
                  command=lambda: master.switchFrame("PageTwo"))
        pageTwoButton.grid(row=0, column=1)
        
        startPageButton = ttk.Button(self, text="Open start page",
                  command=lambda: master.switchFrame("StartPage"))
        startPageButton.grid(row=0, column=2)
















