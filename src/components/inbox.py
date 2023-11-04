"""
    This will control the view which will display the inbox.
    This will contain all the tasks and have the finished tasks crossed out below it.
"""

from tkinter import *
from page import Page
class inboxFrame(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text="Inbox")
        label.pack(side="top", fill="both", expand=True)

       