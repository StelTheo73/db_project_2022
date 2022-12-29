import tkinter as tk
from libraries.Pages.StartPage import StartPage
from libraries.Pages.AddPlayerPage import AddPlayerPage
from libraries.Pages.AddRefereePage import AddRefereePage
from libraries.Pages.AddTeamPage import AddTeamPage
from libraries.Pages.AddMatchPage import AddMatchPage
from libraries.Pages.AddStatPage import AddStatPage
from libraries.Pages.DeletePlayerPage import DeletePlayerPage
from libraries.Pages.DeleteRefereePage import DeleteRefereePage
from libraries.Pages.DeleteTeamPage import DeleteTeamPage
from libraries.Pages.DeleteMatchPage import DeleteMatchPage
from libraries.Pages.DeleteStatPage import DeleteStatPage
from libraries.Pages.StatisticsPage import StatisticsPage

class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self._frames = {
            "StartPage"  : StartPage,
            "Add Player" : AddPlayerPage,
            "Add Referee": AddRefereePage,
            "Add Team"   : AddTeamPage,
            "Add Match"  : AddMatchPage,
            "Add Stat"   : AddStatPage,
            "Delete Player"  : DeletePlayerPage,
            "Delete Referee" : DeleteRefereePage,
            "Delete Team"    : DeleteTeamPage,
            "Delete Match"   : DeleteMatchPage,
            "Delete Stat"    : DeleteStatPage,
            "Statistics"      : StatisticsPage
        }
        
        self.geometry("800x500")
        self.title("My Championship")
        self.minsize(width=550, height=350)

        self.switchFrame("StartPage")

        # Submit on Enter
        #self.bind("<Return>", lambda e: self._frame.onSubmit())

    def switchFrame(self, frame_id):
        """Destroys current frame and replaces it with a new one."""
        frameClass = self._frames[frame_id]

        new_frame = frameClass(self)
        if self._frame:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(expand=True, fill="both")
