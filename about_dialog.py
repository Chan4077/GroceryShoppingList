# import tkSimpleDialog
from tkinter import *
from tkinter import simpledialog as dialog
from tkinter import messagebox as mbox
from sys import version

class AboutDialog(dialog.Dialog):

    def body(self, master):
        # self.minsize(width=200)
        # self.maxsize(width=200)
        self.title("About Grocery List")
        Label(master, text="Made for the purposes of Google's Science Fair 2018").grid(row=0, sticky=W)
        Label(master, text="Python version: {}".format(version)).grid(row=1, sticky=W)
        Label(master, text="Tkinter version: {}".format(TkVersion)).grid(row=2, sticky=W)
        Label(master, text="Copyright Edric Chan. All rights reserved").grid(row=3, sticky=W)
        Label(master, text="This project is licensed with the MIT license.").grid(row=4, sticky=W)
        self.resizable(width=False, height=False)
    def buttonbox(self):
        pass
