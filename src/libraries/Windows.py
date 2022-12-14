import tkinter as tk
from libraries.Pages.StartPage import StartPage
from libraries.Pages.AddPlayerPage import AddPlayerPage
from libraries.Pages.AddRefereePage import AddRefereePage
from libraries.Pages.AddTeamPage import AddTeamPage
from libraries.Pages.AddMatchPage import AddMatchPage
from libraries.Pages.AddStatsPage import AddStatsPage

class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self._frames = {
            "StartPage"  : StartPage,
            "Add Player" : AddPlayerPage,
            "Add Referee": AddRefereePage,
            "Add Team"   : AddTeamPage,
            "Add Match"   : AddMatchPage,
            "Add Stat"   : AddStatsPage,
        }
        
        self.geometry("800x500")
        self.title("My Championship")
        self.minsize(width=500, height=300)

        self.switchFrame("StartPage")

        # Submit on Enter
        self.bind("<Return>", lambda e: self._frame.onSubmit())

    def switchFrame(self, frame_id):
        """Destroys current frame and replaces it with a new one."""
        frameClass = self._frames[frame_id]

        new_frame = frameClass(self)
        if self._frame:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(expand=True, fill="both")
