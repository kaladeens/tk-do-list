"""
    This will control the view which will display the calender.
    Should show the entire month with the current day highlighted, and 
    allow the user to see any tasks they would have on any day.
"""

from tkinter import *
from components import Page

class CalenderFrame(Page):
    def __init__(self,*args,**kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="Calender")
        label.pack(side="top", fill="both", expand=True)