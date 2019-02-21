import tkinter
from tkinter import ttk
from tkinter import messagebox as mbox
from tkinter import simpledialog

from new_grocery_item_dialog import NewGroceryItemDialog
from about_dialog import AboutDialog

from utils import Utils

def cmd_new_grocery_item():
    print("Adding a new shopping item...")
    filemenu.entryconfigure(0, state="disabled")
    dialog = NewGroceryItemDialog(root)
    # d.resizable(False, False)
    # d.minsize(width=300)
    # root.wait_window(Toplevel())
    filemenu.entryconfigure(0, state="normal")
    print(dialog.result)


def cmd_new_grocery_list():
    print("Creating a new shopping list...")
    filemenu.entryconfigure(1, state="disabled")
    # result = simpledialog.askstring(title="New shopping list", prompt="Name of shopping list", parent=root)
    result = simpledialog.askstring(
        title="New shopping list", prompt="Name of shopping list")
    print(result)
    filemenu.entryconfigure(1, state="normal")


def cmd_delete_grocery_list():
    # filemenu.entryconfigure(3, state="disabled")
    print("Deleting grocery list...")
    result = mbox.askokcancel(
        message="Are you sure you want to delete the grocery list?")
    print(result)
    # filemenu.entryconfigure(3, state="normal")


def cmd_delete_grocery_item():
    # filemenu.entryconfigure(4, state="disabled")
    print("Deleting grocery item...")
    result = mbox.askokcancel(
        message="Are you sure you want to delete the grocery item?")
    print(result)
    # filemenu.entryconfigure(4, state="normal")


def cmd_save():
    print("Save")


def cmd_undo():
    print("Undo")


def cmd_about():
    print("About")
    helpmenu.entryconfigure(0, state="disabled")
    d = AboutDialog(root)
    helpmenu.entryconfigure(0, state="normal")


def cmd_github():
    pass


root = tkinter.Tk()
root.title("Grocery List")

root.minsize(width=480, height=270)

menubar = tkinter.Menu(root)

filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="New Grocery Item...", underline=0, accelerator="Command-n",
                     command=cmd_new_grocery_item)
filemenu.add_command(label="New Grocery List...", underline=0, accelerator="Option-Command-n",
                     command=cmd_new_grocery_list)
# filemenu.add_separator()
# filemenu.add_command(label="Delete Grocery List...", underline=0,
#                      accelerator="Command-BackSpace", command=cmd_delete_grocery_list)
# filemenu.add_command(label="Delete Grocery Item...", underline=0,
#                      accelerator="Option-Command-BackSpace", command=cmd_delete_grocery_item)
menubar.add_cascade(label="File", menu=filemenu, underline=0)

# editmenu = tkinter.Menu(menubar, tearoff=0)
# editmenu.add_command(label="Undo", underline=0, accelerator="Ctrl+U",
#                      command=cmd_undo)
# editmenu.add_separator()
# editmenu.add_command(label="Cut", underline=2, accelerator="Ctrl+X",
#                      command=lambda: print("Cut"))
# editmenu.add_command(label="Copy", underline=0, accelerator="Ctrl+C",
#                      command=lambda: print("Copy"))
# editmenu.add_command(label="Paste", underline=0, accelerator="Ctrl+V",
#                      command=lambda: print("Paste"))
# editmenu.add_command(label="Delete", underline=2,
#                      command=lambda: print("Delete"))
# editmenu.add_separator()
# editmenu.add_command(label="Select All", underline=7, accelerator="Ctrl+A",
#                      command=lambda: print("Select All"))
# menubar.add_cascade(label="Edit", menu=editmenu, underline=0)
editmenu = tkinter.Menu(menubar, name="edit", tearoff=0)
menubar.add_cascade(menu=editmenu, label="Edit", underline=0)

viewmenu = tkinter.Menu(menubar, name="view", tearoff=0)
# viewfontsmenu = tkinter.Menu(viewmenu, tearoff=0)
# viewfontsmenu.add_command(label="Reset To Default", accelerator="Command+0")
# viewfontsmenu.add_command(label="Increase By 5%", accelerator="Command++")
# viewfontsmenu.add_command(label="Decrease By 5%", accelerator="Command+-")
# viewappearancemenu = tkinter.Menu(viewmenu, tearoff=0)
# viewappearancemenu.add_cascade(
#     menu=viewfontsmenu, label="Font Size", underline=0, state="disabled")
# viewappearancemenu.add_separator()
# viewappearancemenu.add_checkbutton(label="Read-only Mode")
# viewappearancemenu.add_checkbutton(label="Dark Mode", state="disabled")
# viewmenu.add_separator()
# viewmenu.add_cascade(menu=viewappearancemenu, label="Appearance", underline=0)
# viewmenu.add_cascade(menu=viewfontsmenu, label="Font Size", underline=0)
# viewmenu.add_separator()
menubar.add_cascade(menu=viewmenu, label="View", underline=0)

windowmenu = tkinter.Menu(menubar, name="window", tearoff=0)
menubar.add_cascade(menu=windowmenu, label="Window", underline=0)

helpmenu = tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About My Grocery List...",
                     underline=0, command=cmd_about)
helpmenu.add_command(label="View Source Code", underline=0,
                     command=cmd_github, state="disabled")
helpmenu.add_separator()
helpmenu.add_command(label="Keyboard Shortcuts", state="disabled")
menubar.add_cascade(label="Help", menu=helpmenu, underline=0)

root.config(menu=menubar)

# root.bind("<Control-o>", lambda event: cmd_open())
# root.bind("<Control-s>", lambda event: cmd_save())
# root.bind("<Control-u>", lambda event: cmd_undo())
# root.bind("<F1>", lambda event: cmd_help())
# filemenu.bind("<Command+N>", lambda event: cmd_new_grocery_item)
# filemenu.bind("<Command+Backspace>", lambda event: cmd_delete_grocery_list)

# helloWorldLabel = tkinter.Label(
#     root, text="Hello, Tkinter!", font=("TkTextFont", 60))
# helloWorldLabel.pack(fill="both", expand=True)

weeklyNeeds = ["tomato", "carrot", "potato", "orange"]
# weeklyNeeds = []

weeklyNeedsTree = ttk.Treeview(root)
# weeklyNeedsLb = tkinter.Listbox(root)
for index, weeklyNeed in enumerate(weeklyNeeds):
  weeklyNeedsTree.insert(index=index, text=weeklyNeed, parent="")

weeklyNeedsTreeContextMenu = tkinter.Menu(weeklyNeedsTree, tearoff=0)
weeklyNeedsTreeContextMenu.add_command(label="Delete item", accelerator="Command+BackSpace", command=cmd_delete_grocery_item)

def showPopup(event):
  try:
    weeklyNeedsTreeContextMenu.tk_popup(event.x_root, event.y_root, 0)
  finally:
    weeklyNeedsTreeContextMenu.grab_release()

if Utils.getSystem() == "Darwin":
  weeklyNeedsTree.bind("<Button-2>", showPopup)
  weeklyNeedsTree.bind("<Control-Button-1>", showPopup)
else:
  weeklyNeedsTree.bind("<Button-3>", showPopup)
weeklyNeedsTree.pack(fill="both", expand=True)

root.mainloop()
