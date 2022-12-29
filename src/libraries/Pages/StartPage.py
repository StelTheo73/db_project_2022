import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame

class StartPage(MainFrame):
    def __init__(self, master):
        MainFrame.__init__(self, master)

        tk.Label(self.scrollable_frame, text="Query Page").grid(row=2, column=0)
        self.createQueryFrame().grid(row = 3, column = 0, columnspan = 8, rowspan = 1, sticky = tk.W)

        self.submitButton.grid(row = 4, column = 0)

    def onSubmit(self,):
        super().onSubmit('query')

    def createQueryFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth=5, relief="ridge")
        
        queryLabel = ttk.Label(contentFrame, text = "Query")
        
        queryEntry = ttk.Entry(contentFrame, width=80,\
            validate='key', validatecommand=(contentFrame.register(lambda txt: txt[:7]=='SELECT '), '%P'))
        queryEntry.insert(0, 'SELECT ')
        self.inputs['query'] = queryEntry
        queryEntry.focus_set()

        
        queryLabel.grid(row = 0, column = 0, columnspan = 1, padx = 10, sticky = tk.W)
        queryEntry.grid(row = 1, column = 0, columnspan = 1, padx = 10, sticky = tk.W)

        return contentFrame
