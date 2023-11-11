from components import CalenderFrame
from components import InboxFrame
import tkinter as tk 

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.tk.title("To Do App")
        self.tk.geometry("800x600")
        self.tk.resizable(False, False)

        container = tk.Frame(self)

        self.pages = {}
        self.current_page = None

        for page in (InboxFrame, CalenderFrame):
            pageName = page.__name__
            frame = page(parent = container, controller = self)
            self.pages[pageName] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame("InboxFrame")
    def show_frame(self, pageName):
        frame = self.pages[pageName]
        frame.show()