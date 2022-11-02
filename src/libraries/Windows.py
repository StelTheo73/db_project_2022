import tkinter as tk
import tkinter.ttk as ttk
from libraries.Pages.StartPage import StartPage
from libraries.Pages.AddPlayerPage import AddPlayerPage
from libraries.Pages.AddRefereePage import AddRefereePage

class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self._frames = {
            "StartPage": StartPage,
            "Add Player": AddPlayerPage,
            "Add Referee": AddRefereePage
        }
        
        self.geometry("600x400")
        self.title("My Championship")
        self.minsize(width = 550, height = 200)

        self.switchFrame("StartPage")

    def switchFrame(self, frame_id):
        """Destroys current frame and replaces it with a new one."""
        frameClass = self._frames[frame_id]

        new_frame = frameClass(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(expand = True, fill = "both")