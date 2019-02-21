"""
Task:
1. Input via spreadsheet
2. Compile data into list in a list
3. Ask how should the names be sorted
4. Algorithm to sort names (e.g. by low/medium/high ability or mixed)
EXTRAS
1. Sort by gender on top of the 2 original listings (e.g. 1 female in every grp)
"""

# import random
from tkinter import ttk, Tk, Menu
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import messagebox
from random import shuffle
import csv


def import_from_spreadsheet(event=None):
    print("Event: ", event)
    # See
    # https://www.reddit.com/r/learnpython/comments/3loul5/only_showing_certain_filetypes_in_filedialog/cv9eaey
    # for more info
    ftypes = [
        ("Legacy Excel worksheet", "*.xls"),
        ("Excel workbook", "*.xlsx"),
        ("Comma-separated value file", "*.csv")
    ]
    root.update()
    filename = askopenfilename(parent=root, title="Import spreadsheet", filetypes=ftypes)
    root.update()
    try:
        # print(filename)
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            spreadsheet_list = list(reader)
            spreadsheet_list.pop(0)
            print("Spreadsheet list: ", spreadsheet_list)
            shuffle(spreadsheet_list)
            print("Shuffled spreadsheet list: ", spreadsheet_list)
    except FileNotFoundError:
        messagebox.showerror("Spreadsheet not found", "Please select a spreadsheet to import!")


def sort_separate_ability(spreadsheet_list):
    pass


def sort_mixed_ability():
    pass


def sort_female():
    pass


def export_results():
    pass


root = Tk()
root.title("Student Grouper")
tree_view = ttk.Treeview(root, columns=("name", "gender", "ability"), show="headings")
tree_view.pack(fill="both", expand=True)
tree_view.heading("name", text="Name")
tree_view.heading("gender", text="Gender")
tree_view.heading("ability", text="Ability")
tree_view.column("name", width=150)
tree_view.column("gender", width=60)
tree_view.column("ability", width=70)

"""
abilities = ["L", "H", "M"]
genders = ["F", "M"]
for i in range(0, 25):
    gender = random.choice(genders)
    ability = random.choice(abilities)

    tree_view.insert("", "end", values=("Student #{}".format(i), gender, ability))
"""

root.minsize(width=480, height=270)

# The menu bar
menubar = Menu(root)

# File menu
filemenu = Menu(menubar, name="file", tearoff=0)
filemenu.add_command(label="Import from Spreadsheet...", underline=0, accelerator="Command-o",
                     command=import_from_spreadsheet)
root.bind_all("<Command-o>", import_from_spreadsheet)

filemenu.add_command(label="Export Results...", underline=0, accelerator="Command-e", command=export_results)
menubar.add_cascade(label="File", menu=filemenu, underline=0)

# Edit menu
editmenu = Menu(menubar, name="edit", tearoff=0)
menubar.add_cascade(menu=editmenu, label="Edit", underline=0)

# View menu
viewmenu = Menu(menubar, name="view", tearoff=0)
menubar.add_cascade(menu=viewmenu, label="View", underline=0)

# Window menu
windowmenu = Menu(menubar, name="window", tearoff=0)
menubar.add_cascade(menu=windowmenu, label="Window", underline=0)

# Help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Keyboard Shortcuts", state="disabled")
menubar.add_cascade(label="Help", menu=helpmenu, underline=0)

root.config(menu=menubar)

root.mainloop()
