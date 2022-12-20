import tkinter as tk
import tkinter.ttk as ttk
from libraries.Pages.DeletePersonPage import DeletePersonPage
from libraries.dbIO.QuerySelector import QuerySelector

class DeletePlayerPage(DeletePersonPage):
    def __init__(self, master):
        DeletePersonPage.__init__(self, master, personType="Player")
