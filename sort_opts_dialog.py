from tkinter import Frame, simpledialog, OptionMenu, Label, StringVar

OPTIONS = [
    "Ability",
    "Mixed Ability"
]


class SortOptionsDialog(simpledialog.Dialog):
    def body(self, master: Frame):
        self.selectSortByVal = StringVar(master)
        self.selectSortByVal.set(OPTIONS[0])
        Label(master, text="Sort by:").grid(row=0)
        self.selectSortBy = OptionMenu(master, self.selectSortByVal, *OPTIONS)
        self.selectSortBy.grid(row=0, column=1, padx=10, pady=10)

    def apply(self):
        self.result = {"sortBy": self.selectSortByVal.get()}
