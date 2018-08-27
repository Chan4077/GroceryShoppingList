# import tkSimpleDialog
from tkinter import *
from tkinter import simpledialog as dialog
from tkinter import messagebox as mbox

class AboutDialog(dialog.Dialog):

    def body(self, master):
        # self.minsize(width=200)
        # self.maxsize(width=200)
        self.title("About Grocery List")
        Label(master, text="Made for the purposes of Google's Science Fair 2018").grid(row=0, sticky=W)
        Label(master, text="Made using Python 3 and Tkinter").grid(row=1, sticky=W)
        self.resizable(width=False, height=False)
    def buttonbox(self):
        pass
