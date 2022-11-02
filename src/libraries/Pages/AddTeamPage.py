import tkinter as tk
import tkinter.ttk as ttk
from libraries.Autocomplete.AutocompleteEntry import AutocompleteCombobox, AutocompleteEntry
from libraries.MainFrame import MainFrame

class AddTeamPage(MainFrame):
    def __init__(self, master, personType=""):
        MainFrame.__init__(self, master)

        teamInfoFrame = self.createTeamInfoFrame(self.scrollable_frame)

    def createTeamInfoFrame(self, container):
        contentFrame = ttk.Frame(container, borderwidth = 5, relief = "ridge")

        nameLabel = ttk.Label(contentFrame, text = "Name")
        nameEntry = ttk.Entry(contentFrame)
        nameEntry.focus_set()

        stadiumLabel = ttk.Label(contentFrame)
        stadiumEntry = ttk.Entry(contentFrame)
        
        nameEntry.grid(row = 1)

        return contentFrame