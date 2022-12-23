import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame
from libraries.dbIO.DbQueries import QuerySelector

class DeleteRefereePage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)
        self.create_type_selector().grid(row = 2, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        self.referee_selector = self.create_referee_selector("")
        self.referee_selector.grid(row = 12, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
        self.submitButton.grid(row = 50, column = 0)

    def onSubmit(self):
        super().onSubmit('delete_referee')

    def create_type_selector(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")

        typeLabel = ttk.Label(contentFrame, text = "Select type")
        typeSelector = ttk.Combobox(contentFrame, state = "readonly")
        typeSelector["values"] = QuerySelector.getRefPositions()
        self.inputs["type"] = typeSelector

        typeSelectorButton = ttk.Button(contentFrame, text = "Select",
                        command= self.select_type)

        typeLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        typeSelector.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        typeSelectorButton.grid(row = 2, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame

    def create_referee_selector(self, type):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth = 5, relief = "ridge")
        refereeLabel = ttk.Label(contentFrame, text = "Select referee")
        
        print(type)
        refereeSelector = ttk.Combobox(contentFrame, state = "readonly")
        refereeSelector["values"] = QuerySelector.getRefereesByType(type)
        self.inputs["referee"] = refereeSelector
        
        refereeLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        refereeSelector.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame

    def select_type(self):
        type = {func: self.inputs[func].get() for func in self.inputs}["type"]
        self.referee_selector.destroy()
        self.referee_selector = self.create_referee_selector(type)
        self.referee_selector.grid(row = 12, column = 0, columnspan = 6, rowspan = 10, sticky = tk.W)
