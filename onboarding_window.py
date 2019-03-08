"""
The initial onboarding UI shown when a user launches the app for the first time.
"""
import csv
from tkinter import ttk, constants, Menu, Tk, Toplevel
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

import xlrd

from sort_results_window import SortResultsWindow
from utils import Utils


class OnboardingWindow:
    def __init__(self, parent: Tk):
        self.parent = parent
        self.parent.title("Welcome")
        self.parent.resizable(False, False)
        self.frame = ttk.Frame(parent)
        self.onboarding_welcome_label = ttk.Label(self.frame, text="Welcome to the student grouper!\nChoose an "
                                                                   "action below to get started.",
                                                  font=('Helvetica', 20))
        self.onboarding_welcome_label.pack(padx=20, pady=20)
        self.import_from_spreadsheet_button = ttk.Button(self.frame, text="Import spreadsheet...",
                                                         command=self.import_from_spreadsheet)
        self.import_from_spreadsheet_button.pack(side=constants.BOTTOM, pady=20)
        self.frame.pack(expand=True, fill=constants.BOTH)
        self.menubar = Menu(self.parent)

        self.filemenu = Menu(self.menubar, name="file", tearoff=0)
        self.filemenu.add_command(
            label="Import Spreadsheet...",
            underline=0,
            accelerator="Command-o",
            command=self.import_from_spreadsheet
        )
        self.parent.bind_all("<Command-o>", self.import_from_spreadsheet)

        self.menubar.add_cascade(menu=self.filemenu, label="File", underline=0)

        # View menu
        self.viewmenu = Menu(self.menubar, name="view", tearoff=0)
        self.menubar.add_cascade(menu=self.viewmenu, label="View", underline=0)

        # Window menu
        self.windowmenu = Menu(self.menubar, name="window", tearoff=0)
        self.menubar.add_cascade(menu=self.windowmenu, label="Window", underline=0)

        # Help menu
        self.helpmenu = Menu(self.menubar, name="help", tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu, underline=0)

        self.parent.config(menu=self.menubar)

    def import_from_spreadsheet(self, event=None):
        self.set_import_spreadsheet_menu_item_state("disabled")
        # See
        # https://www.reddit.com/r/learnpython/comments/3loul5/only_showing_certain_filetypes_in_filedialog/cv9eaey
        # for more info
        ftypes = [
            ("Legacy Excel worksheet", "*.xls"),
            # TODO: Implement XLSX support
            # Currently, xlwt does not support XLSX files
            # ("Excel workbook", "*.xlsx"),
            ("Comma-separated value file", "*.csv"),
            # TODO: Implement TSV support
            ("Tab-separated value file", "*.tsv")
            # ("All files", "*")
        ]
        filename = askopenfilename(parent=self.parent, title="Import spreadsheet", filetypes=ftypes)
        if filename is not None:
            # Retrieve the file extension
            fileext = Utils.get_file_ext(filename)
            if fileext == "csv":
                try:
                    with open(filename, "r") as f:
                        reader = csv.reader(f)
                        spreadsheet_list = list(reader)
                        # Ignore the first row (assume that there's a heading row)
                        spreadsheet_list.pop(0)

                        # Open a new window for the sort results window
                        sort_results_parent = Toplevel(self.parent)
                        sort_results_window = SortResultsWindow(sort_results_parent, spreadsheet_list,
                                                                Utils.get_file_name(filename))
                except FileNotFoundError:
                    print("File not found! {}".format(filename))
            elif fileext == "tsv":
                try:
                    with open(filename, "r") as f:
                        reader = csv.reader(f, delimiter="\t")
                        spreadsheet_list = list(reader)
                        # Ignore the first row (assume that there's a heading row)
                        spreadsheet_list.pop(0)

                        # Open a new window for the sort results window
                        sort_results_parent = Toplevel(self.parent)
                        sort_results_window = SortResultsWindow(sort_results_parent, spreadsheet_list,
                                                                Utils.get_file_name(filename))
                except FileNotFoundError:
                    print("File not found! {}".format(filename))
            elif fileext == "xls":
                workbook = xlrd.open_workbook(filename)
                if workbook.nsheets > 0:
                    sheet = workbook.sheet_by_index(0)
                    spreadsheet_list = []
                    for i in range(1, sheet.nrows):
                        # Ignore the first row
                        spreadsheet_list.append(sheet.row_values(i))

                    # Open a new window for the sort results window
                    sort_results_parent = Toplevel(self.parent)
                    sort_results_window = SortResultsWindow(sort_results_parent, spreadsheet_list,
                                                            Utils.get_file_name(filename))
                else:
                    showerror(message="The spreadsheet specified has no sheets!")

        else:
            print("User either cancelled the dialog or pressed the cancel button.")
        self.set_import_spreadsheet_menu_item_state("normal")

    def set_import_spreadsheet_menu_item_state(self, state):
        self.filemenu.entryconfig(0, state=state)
