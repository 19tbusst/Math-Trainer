from tkinter import *


root = Tk()


def opSet():
    op = opQuestion.get()
    global difQ
    global difText
    global difButton

    if op == "+" or op == "-" or op == "*" or op == "/":
        welcomeText.grid_forget()
        opQuestion.grid_forget()
        opButton.grid_forget()
        difText = Label(root, text="What difficulty do\nyou want to train at?")
        difQ = Entry(root)
        difQ.insert(0, "Easy Medium or Hard")
        difButton = Button(root, text="Done", command=difSet)

        difButton.grid(row=2, column=0)
        difQ.grid(row=1, column=0)
        difText.grid(row=0, column=0)


def difSet():
    dif = difQ.get()
    if dif.lower() != "easy" and dif.lower() != "medium" and dif.lower() != "hard":
        print("That is not an option")

    else:
        difButton.grid_forget()
        difText.grid_forget()
        difQ.grid_forget()


opButton = Button(root, text="Done", command=opSet)
welcomeText = Label(root, text="Welcome to Math Trainer!\nwhat do you want to practice?")
opQuestion = Entry(root)
opQuestion.insert(0, "+, -, * or /")

welcomeText.grid(row=0, column=0)
opQuestion.grid(row=1, column=0)
opButton.grid(row=2, column=0)

root.mainloop()

