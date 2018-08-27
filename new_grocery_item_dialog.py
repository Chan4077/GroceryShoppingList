# import tkSimpleDialog
from tkinter import *
from tkinter import simpledialog as dialog
from tkinter import messagebox as mbox

def dosomething(stuff):
    print(stuff)

class NewGroceryItemDialog(dialog.Dialog):

    def body(self, master):

        Label(master, text="Grocery item:").grid(row=0, sticky=W)
        Label(master, text="Quantity:").grid(row=1, sticky=W)

        self.e1 = Entry(master)
        self.e2 = Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.resizable(width=False, height=False)
    def validate(self):
        try:
            second = int(self.e2.get())
            self.result = self.e1.get(), second
            if second < 0:
                raise ValueError()
            if not self.e1.get():
                raise TypeError
            return 1
        except ValueError:
            mbox.showerror(message="Please specify a positive number!")
            return 0
        except TypeError:
            mbox.showerror(message="Please specify a grocery item!")
            return 0

    def apply(self):
        return self.result
