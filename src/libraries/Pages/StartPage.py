import tkinter as tk
import tkinter.ttk as ttk
from libraries.MainFrame import MainFrame

class StartPage(MainFrame):
    def __init__(self, master):
        ## Let's make this the page where the user can give his queries
        MainFrame.__init__(self, master)
        self.inputs = {}

        #tk.Label(self, text="This is the Start Page").pack(side="top", fill="x", pady=10)
        tk.Label(self.scrollable_frame, text="This is the Start Page").grid(row=1, column=1)
        self.createQueryFrame().grid(row = 2, column = 1, columnspan = 8, rowspan = 1, sticky = tk.W)
    
    def onSubmit(self,):
        return super().onSubmit(self.inputs, 'query')

    def createQueryFrame(self):
        contentFrame = ttk.Frame(self.scrollable_frame, borderwidth=5, relief="ridge")
        
        queryLabel = ttk.Label(contentFrame, text = "Query")
        
        queryEntry = ttk.Entry(contentFrame, width=80,\
            validate='key', validatecommand=(contentFrame.register(lambda txt: txt[:7]=='SELECT '), '%P'))
        queryEntry.insert(0, 'SELECT ')
        self.inputs['query'] = queryEntry
        queryEntry.focus_set()

        
        queryLabel.grid(row = 0, column = 0, columnspan = 2, padx = 10, sticky = tk.W)
        queryEntry.grid(row = 1, column = 0, columnspan = 2, padx = 10, sticky = tk.W)

        return contentFrame
