"""
Window to represent the results of the sort
"""
import csv
from tkinter import Menu, Tk, ttk, StringVar
from tkinter.constants import N, S, E, W, CENTER
from tkinter.filedialog import asksaveasfilename
from tkinter.messagebox import showerror
from tkinter.simpledialog import askinteger
from typing import List

import xlwt

from sorting_algorithm import SortingAlgorithm
from utils import Utils


class SortResultsWindow:
    def __init__(self, parent: Tk, data: List[List[str]], filename: str):
        self.parent = parent
        self.data = data
        self.sorted_data = []
        self.sorted_data_headings = []
        self.parent.title(filename)

        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_rowconfigure(0, weight=1)

        self.main_frame = ttk.Frame(self.parent, padding=(3, 3, 12, 12))
        self.main_frame.grid(column=0, row=0, sticky=(N, S, E, W))
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Initialise the treeview
        self.render_data()

        self.sort_opts_moved_frame = ttk.Frame(self.main_frame)
        self.sort_opts_moved_frame.grid(column=0, row=1, sticky=(N, S, E, W))
        # self.sort_opts_moved_frame_title_label.grid(column=0, row=0)
        self.sort_opts_moved_frame_message_label = ttk.Label(self.sort_opts_moved_frame,
                                                             text="Sorting options have moved to the file menu!\nTo access the sorting options, go to File > Sort By.")
        # self.sort_opts_moved_frame_message_label.grid(column=0, row=1)
        self.sort_opts_moved_frame_message_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        """
        self.sort_by_frame = ttk.Frame(self.main_frame)
        self.sort_by_frame.grid(column=0, row=1, sticky=(N, S, E, W))
        self.sort_by_frame_label = ttk.Label(self.sort_by_frame, text="Sort by:")
        self.sort_by_frame_label.grid(column=0, row=0)
        self.sort_by_frame_ability_button = ttk.Button(self.sort_by_frame, text="Ability", command=self.sort_by_ability)
        self.sort_by_frame_ability_button.grid(column=0, row=1)
        self.sort_by_frame_mixed_ability_button = ttk.Button(self.sort_by_frame, text="Mixed Ability",
                                                             command=self.sort_by_mixed_ability)
        self.sort_by_frame_mixed_ability_button.grid(column=1, row=1)
        """
        # self.main_frame.grid_rowconfigure(0, weight=1)r
        # self.main_frame.grid_rowconfigure(2, weight=1)
        # self.main_frame.grid_columnconfigure(0, weight=1)
        # self.main_frame.grid_columnconfigure(2, weight=1)

        self.parent.minsize(width=480, height=270)

        # The menu bar
        self.menubar = Menu(parent)

        # File menu
        self.filemenu = Menu(self.menubar, name="file", tearoff=0)
        self.filemenu.add_command(label="Export Results...", underline=0, accelerator="Command-s",
                                  command=self.export_results, state="disabled")
        self.filemenu.add_separator()
        # self.filemenu.add_command(label="Revert To Original List", underline=0, accelerator="Command-z",
        #                      command=self.revert_to_original)
        self.sortbymenu = Menu(self.filemenu, tearoff=0)
        self.abilitytextvar = StringVar(master=self.parent, value="none")
        self.sortbymenu.add_radiobutton(label="None", variable=self.abilitytextvar, value="none", underline=0,
                                        command=self.revert_original)
        self.sortbymenu.add_radiobutton(label="Ability", variable=self.abilitytextvar, value="ability", underline=0,
                                        command=self.sort_by_ability)
        self.sortbymenu.add_radiobutton(label="Mixed Ability...", variable=self.abilitytextvar, value="mixed",
                                        underline=0,
                                        command=self.sort_by_mixed_ability)
        self.filemenu.add_cascade(label="Sort By", menu=self.sortbymenu, underline=0)
        # Initially disable saving as there is currently no data to export
        self.parent.bind_all("<Command-s>", self.export_results)
        # self.parent.bind_all("<Command-z>", self.revert_to_original)

        self.menubar.add_cascade(label="File", menu=self.filemenu, underline=0)

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

        self.algorithm = SortingAlgorithm(data)

    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, command=lambda _col=col: self.treeview_sort_column(tv, _col, not reverse))

    def export_results(self, event=None):
        ftypes = [
            ("Legacy Excel worksheet", "*.xls"),
            # TODO: Implement XLSX support
            # xlwt does not support xlsx files for now
            # ("Excel workbook", "*.xlsx"),
            ("Comma-separated value file", "*.csv"),
            ("Tab-separated value file", "*.tsv")
        ]
        filename = asksaveasfilename(
            parent=self.parent,
            title="Save results as",
            filetypes=ftypes,
            initialfile="student_grouper_results"
        )

        with open(filename, "w") as file:
            fileext = Utils.get_file_ext(filename)
            if fileext == "xls":
                workbook = xlwt.Workbook()
                sheet = workbook.add_sheet("Student Grouper Results")
                print("Sorted data headings:", self.sorted_data_headings)
                # print("Sorted data:", list(self.sorted_data))
                for index, item in enumerate(self.sorted_data):
                    print("Index:", index)
                    print("Item:", item)
                    row = sheet.row(index)
                    for itemindex, nesteditem in enumerate(item):
                        print("Item index:", itemindex)
                        print("Nested item:", nesteditem)
                        print("Nested item type:", type(nesteditem))
                        print("Index:", index)
                        print("Item:", item)
                        row.write(itemindex, nesteditem)
                workbook.save(file)

            elif fileext == "csv":
                file_writer = csv.writer(file)
                file_writer.writerow(list(self.sorted_data_headings))
                file_writer.writerows(list(self.sorted_data))
            elif fileext == "tsv":
                file_writer = csv.writer(file, delimiter="\t")
                file_writer.writerow(list(self.sorted_data_headings))
                file_writer.writerows(list(self.sorted_data))
            else:
                print("File extension {} is not supported!".format(fileext))

    def revert_original(self, event=None):
        """
        Reverts to the original list of data
        :param event: The event of a menu item
        """
        self.render_data(event, destroy_tree_view=True)

    def render_data(self, event=None, destroy_tree_view=False):
        """
        Renders the data as a table
        :param event: The event of a menu item
        :param destroy_tree_view: Whether to destroy the tree view
        """
        if destroy_tree_view and self.tree_view is not None:
            self.tree_view.destroy()
        self.tree_view = ttk.Treeview(self.main_frame, columns=("name", "ability", "gender"), show="headings")
        self.tree_view.grid(column=0, row=0, sticky=(N, S, E, W))
        for col in self.tree_view["columns"]:
            self.tree_view.heading(col, text=col.capitalize(),
                                   command=lambda _col=col: self.treeview_sort_column(self.tree_view, _col, False))
        self.tree_view.column("name", width=150)
        self.tree_view.column("gender", width=60)
        self.tree_view.column("ability", width=70)

        for data_item in self.data:
            name = data_item[0]
            ability = ""
            gender = ""
            if data_item[1].lower() in ["l", "low"]:
                ability = "Low"
            elif data_item[1].lower() in ["m", "medium"]:
                ability = "Medium"
            elif data_item[1].lower() in ["h", "high"]:
                ability = "High"
            if data_item[2].lower() in ["f", "female"]:
                gender = "Female"
            elif data_item[2].lower() in ["m", "male"]:
                gender = "Male"

            self.tree_view.insert("", "end", values=(name, ability, gender))

    def sort_by_ability(self, event=None):
        if event is not None:
            print(event)
            return
        # Use sorting algorithm for ability
        print("Data in algorithm class:", self.algorithm.data)
        print("Low data in algorithm class:", self.algorithm.low)
        print("Middle data in algorithm class:", self.algorithm.middle)
        print("High data in algorithm class:", self.algorithm.high)
        sorted_list = self.algorithm.sort_ability()

        # Reinitialise the tree view
        self.tree_view.destroy()
        self.tree_view = ttk.Treeview(self.main_frame, columns=("high", "medium", "low"), show="headings")
        self.tree_view.grid(column=0, row=0, sticky=(N, S, E, W))
        for column in self.tree_view["columns"]:
            self.tree_view.heading(column, text="{} ability".format(column.capitalize()))

        # Code for displaying data in columns
        names = map(list, zip(*sorted_list))
        # Insert the data into the tree view
        for name_list in names:
            self.tree_view.insert("", "end", values=tuple(name_list))

        # And set the sorted data to the result of the sorting algorithm
        self.sorted_data = map(list, zip(*sorted_list))
        self.sorted_data_headings = ["High", "Medium", "Low"]
        # Reenable export result menu item
        self.filemenu.entryconfig(0, state="normal")

    def sort_by_mixed_ability(self, event=None):
        if event is not None:
            print(event)
            return
        groups = askinteger("Prompt", "Enter the number of groups:")
        # askinteger returns None if the user pressed the cancel button or escaped the dialog
        if groups is not None:
            if groups <= 0:
                showerror(title="Error", message="Please enter a number which is higher than 0!")
                self.sort_by_mixed_ability()
            else:
                print("Data in algorithm class:", self.algorithm.data)
                print("Low data in algorithm class:", self.algorithm.low)
                print("Middle data in algorithm class:", self.algorithm.middle)
                print("High data in algorithm class:", self.algorithm.high)
                sorted_mixed_list = self.algorithm.sort_mixed(groups)
                print(sorted_mixed_list)
                self.tree_view.destroy()
                columns = tuple("group-{}".format(i) for i in range(1, groups + 1))
                self.tree_view = ttk.Treeview(self.main_frame, columns=columns, show="headings")
                self.tree_view.grid(column=0, row=0, sticky=(N, S, E, W))
                for i in range(1, groups + 1): self.tree_view.heading("group-{}".format(i), text="Group {}".format(i))

                # names = [tuple(list(x)[0]) for x in zip(*sorted_mixed_list)]
                names = map(list, zip(*sorted_mixed_list))
                for name in names:
                    self.tree_view.insert("", "end", values=tuple(name))

                self.sorted_data = map(list, zip(*sorted_mixed_list))
                self.sorted_data_headings = ["Group {}".format(i) for i in range(1, groups + 1)]
                # Reenable export result menu item
                self.filemenu.entryconfig(0, state="normal")
