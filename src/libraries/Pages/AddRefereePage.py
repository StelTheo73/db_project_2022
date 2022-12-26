import tkinter as tk
import tkinter.ttk as ttk
from libraries.Pages.AddPersonPage import AddPersonPage
from libraries.dbIO.DbQueries import QuerySelector

class AddRefereePage(AddPersonPage):
    def __init__(self, master):
        AddPersonPage.__init__(self, master, personType = "Referee")

        self.refInfoFrame = self.createRefInfoFrame()

        tk.Label(self.scrollable_frame, text = "Type Info").grid(row = 17, column = 0, sticky = tk.W)
        self.refInfoFrame.grid(row = 18, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
    
        self.submitButton.grid(row = 50, column = 0)
    
    def createRefInfoFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")
        
        positionsLabel = ttk.Label(contentFrame, text = "Type")
        positionSelector = ttk.Combobox(contentFrame, state = "readonly")
        positionSelector["values"] = QuerySelector.getRefPositions()
        self.inputs["type"] = positionSelector

        positionsLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        positionSelector.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame
