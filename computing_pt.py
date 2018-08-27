import tkinter
from tkinter import ttk
from tkinter import messagebox as mbox
from new_grocery_item_dialog import NewGroceryItemDialog
from about_dialog import AboutDialog

def cmd_new_grocery_item():
    print("Adding a new shopping item...")
    filemenu.entryconfigure(0, state="disabled")
    d = NewGroceryItemDialog(root)
    # d.resizable(False, False)
    # d.minsize(width=300)
    # root.wait_window(Toplevel())
    filemenu.entryconfigure(0, state="normal")
    # print(d.result)

def cmd_delete_grocery_list():
    print("Deleting grocery list...")
    result = mbox.askokcancel(message='Are you sure you want to delete the grocery list?')
    print(result)
def cmd_save():
    print("Save")


def cmd_undo():
    print("Undo")

def cmd_bring_to_front():
    root.lift()

def cmd_about():
    print("About")
    helpmenu.entryconfigure(1, state="disabled")
    d = AboutDialog(root)
    helpmenu.entryconfigure(1, state="normal")

root = tkinter.Tk()
root.title("Grocery list")

root.minsize(width=480, height=270)

menubar = tkinter.Menu(root)

filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="New grocery item...", underline=0, accelerator="Command+n",
                     command=cmd_new_grocery_item)
filemenu.add_command(label="Delete grocery list...", underline=0, accelerator="Command+BackSpace",
                     command=cmd_delete_grocery_list)
filemenu.add_separator()
filemenu.bind_all("<Command-n>", lambda event: cmd_new_grocery_item)
filemenu.bind_all("<Command-BackSpace>", lambda event: cmd_delete_grocery_list)
menubar.add_cascade(label="File", menu=filemenu, underline=0)

editmenu = tkinter.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", underline=0, accelerator="Ctrl+U",
                     command=cmd_undo)
editmenu.add_separator()
editmenu.add_command(label="Cut", underline=2, accelerator="Ctrl+X",
                     command=lambda: print("Cut"))
editmenu.add_command(label="Copy", underline=0, accelerator="Ctrl+C",
                     command=lambda: print("Copy"))
editmenu.add_command(label="Paste", underline=0, accelerator="Ctrl+V",
                     command=lambda: print("Paste"))
editmenu.add_command(label="Delete", underline=2,
                     command=lambda: print("Delete"))
editmenu.add_separator()
editmenu.add_command(label="Select All", underline=7, accelerator="Ctrl+A",
                     command=lambda: print("Select All"))
menubar.add_cascade(label="Edit", menu=editmenu, underline=0)

windowmenu = tkinter.Menu(menubar, name='window')
menubar.add_cascade(menu=windowmenu, label='Window')

helpmenu = tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About My Grocery List...", underline=0, accelerator="F1",
                     command=cmd_about)
menubar.add_cascade(label="Help", menu=helpmenu, underline=0)

root.config(menu=menubar)

# root.bind('<Control-o>', lambda event: cmd_open())
# root.bind('<Control-s>', lambda event: cmd_save())
# root.bind('<Control-u>', lambda event: cmd_undo())
# root.bind('<F1>', lambda event: cmd_help())
# filemenu.bind("<Command+N>", lambda event: cmd_new_grocery_item)
# filemenu.bind("<Command+Backspace>", lambda event: cmd_delete_grocery_list)

helloWorldLabel = tkinter.Label(root, text="Hello, World!", font=("TkTextFont", 60))
helloWorldLabel.pack(fill="both", expand=True)

root.mainloop()
