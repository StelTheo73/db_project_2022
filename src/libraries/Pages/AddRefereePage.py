import tkinter as tk
import tkinter.ttk as ttk
from libraries.Autocomplete.AutocompleteEntry import AutocompleteCombobox, AutocompleteEntry
from libraries.Pages.AddPersonPage import AddPersonPage
from libraries.dbIO.QuerySelector import QuerySelector

class AddRefereePage(AddPersonPage):
    def __init__(self, master):
        AddPersonPage.__init__(self, master, personType = "Referee")
        tk.Label(self.scrollable_frame, text="Add Referee").grid(row=1, column=0, sticky = tk.W)