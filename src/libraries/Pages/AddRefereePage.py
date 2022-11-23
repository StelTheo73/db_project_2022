import tkinter as tk
import tkinter.ttk as ttk
from libraries.Pages.AddPersonPage import AddPersonPage
from libraries.dbIO.QuerySelector import QuerySelector

class AddRefereePage(AddPersonPage):
    def __init__(self, master):
        AddPersonPage.__init__(self, master, personType = "Referee")
        tk.Label(self.scrollable_frame, text="Add Referee").grid(row=1, column=0, sticky = tk.W)

        self.refInfoFrame = self.createRefInfoFrame(self.scrollable_frame)

        tk.Label(self.scrollable_frame, text = "Team Info").grid(row = 17, column = 0, sticky = tk.W)
        self.refInfoFrame.grid(row = 18, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
    
    
    def createRefInfoFrame(self, container):
        contentFrame = ttk.Frame(container, borderwidth = 5, relief = "ridge")
        
        positionsLabel = ttk.Label(contentFrame, text = "Position")
        positionSelector = ttk.Combobox(contentFrame, state = "readonly")
        positionSelector["values"] = QuerySelector.getRefPositions()
        self.inputs["position"] = positionSelector

        positionsLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        positionSelector.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame
