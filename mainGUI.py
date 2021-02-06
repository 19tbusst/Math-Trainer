from tkinter import *

root = Tk()


def addOp():
    op = "+"


def subOp():
    op = "-"


def divOp():
    op = "/"


def multOp():
    op = "*"


welcomeL = Label(text="Welcome to Math Trainer,\nwhat do you want to practice?")
addB = Button(text="+", command=addOp, padx=12)
subB = Button(text="-", command=subOp, padx=12)
multB = Button(text="*", command=divOp, padx=12)
divB = Button(text="/", command=multOp, padx=12)


welcomeL.grid(row=0, column=0, columnspan=4)
addB.grid(row=1, column=0)
subB.grid(row=1, column=1)
divB.grid(row=1, column=2)
multB.grid(row=1, column=3)

root.mainloop()
