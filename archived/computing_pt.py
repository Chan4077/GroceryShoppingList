from tkinter import ttk
import tkinter

root = tkinter.Tk()
root.title("Homework Assigner")

root.minsize(480, 270)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

mainFrame = ttk.Frame(root)
questionButtonFrame = ttk.Frame(root)

mainFrame.grid(row=0, column=0, sticky="nsew", relief='flat', borderwidth=4)
questionButtonFrame.grid(row=1, column=0, sticky="nsew", relief='flat', borderwidth=4)

homeworkName = tkinter.StringVar()
questionLabel = ttk.Label(mainFrame, text="What's your homework?")
questionLabel.pack()

questionAnswer = ttk.Entry(mainFrame, textvariable=homeworkName)
questionAnswer.pack()

# questionButtonFrame.place(rely=1.0, relx=1.0, x=0, y=0, anchor=tkinter.SE)

questionCancel = ttk.Button(questionButtonFrame, text="Cancel")
questionCancel.pack(side="right", fill=tkinter.X)

questionOk = ttk.Button(questionButtonFrame, text="OK")
questionOk.pack(side="right", fill=tkinter.X)

# questionButtonFrame.pack(fill=tkinter.X, expand=True, side="bottom")

# mainFrame.pack()
# questionButtonFrame.pack()

root.mainloop()
