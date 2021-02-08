from tkinter import *
import random
import time

root = Tk()

dif = 0
times = 0
op = 0
difN = [0, 0]
correct = 0


def addOp():
    global op
    op = "+"
    clear()
    difSelect()

def subOp():
    global op
    op = "-"
    clear()
    difSelect()


def divOp():
    global op
    op = "/"
    clear()
    difSelect()


def multOp():
    global op
    op = "*"
    clear()
    difSelect()


def clear():
    list = root.grid_slaves()
    for l in list:
        l.grid_forget()


def easy():
    global dif
    dif = "easy"
    clear()
    qCount()


def medium():
    global dif
    dif = "medium"
    clear()
    qCount()


def hard():
    global dif
    dif = "hard"
    clear()
    qCount()


def difSelect():
    difL = Label(root, text="What difficulty do\nyou want to train at?")
    easyB = Button(root, text="Easy", command=easy)
    mediumB = Button(root, text="Medium", command=medium)
    hardB = Button(root, text="Hard", command=hard)

    difL.grid(row=0, column=0, columnspan=3)
    easyB.grid(row=1, column=0)
    mediumB.grid(row=1, column=1)
    hardB.grid(row=1, column=2)


def qCount():
    global qE
    global qL
    root.bind('<Return>', qFinalize)
    qL = Label(root, text="How many questions\ndo you want?")
    qE = Entry(root)
    qB = Button(root, text="Done", command=qFinalize)

    qL.grid(row=0, column=0)
    qE.grid(row=1, column=0)
    qB.grid(row=2, column=0)


def qFinalize(e):
    try:
        global times
        global timesFinal
        global tStart

        tStart = time.time()
        times = int(qE.get())
        timesFinal = int(qE.get())
        if times <= 0:
            qL.grid_forget()
            qErrorL = Label(root, text="That's not a \npositive number")
            qErrorL.grid(row=0, column=0)

        else:
            clear()
            qGen()

    except ValueError:
        qL.grid_forget()
        qErrorL = Label(root, text="That's not a number")

        qErrorL.grid(row=0, column=0)


def qAnswer(e):
    try:
        global correct
        qTime = round(time.time() - qStart, 2)
        pAns = askE.get()
        clear()
        if int(pAns) == ans:
            ansL = Label(root, text="Correct! that took " + str(qTime) + " seconds")
            ansL.grid(row=0, column=0)
            correct += 1

        else:
            ansL = Label(root, text="Wrong")
            ansL.grid(row=0, column=0)

        root.update()
        time.sleep(1)
        clear()
        qGen()

    except ValueError:
        ansL = Label(root, text="Wrong")
        ansL.grid(row=0, column=0)

        root.update()
        time.sleep(1)
        clear()
        qGen()

def end():
    sys.exit("Finished")


def restart():
    clear()
    start()


def qGen():
    global times, askE, ans, qStart

    if dif == "easy" and op == "+" or op == "-":
        difN = [1, 20]

    elif dif == "medium" and op == "+" or op == "-":
        difN = [3, 50]

    elif dif == "hard" and op == "+" or op == "-":
        difN = [6, 100]

    elif dif == "easy" and op == "*" or op == "/":
        difN = [1, 5]

    elif dif == "medium" and op == "*" or op == "/":
        difN = [3, 10]

    elif dif == "hard" and op == "*" or op == "/":
        difN = [5, 20]

    else:
        print("Error")

    training = True
    while training:
        q1 = (random.randint(difN[0], difN[1]))
        q2 = (random.randint(difN[0], difN[1]))

        if op == "+":
            ans = q1 + q2

        elif op == "-":
            ans = q1 - q2

        elif op == "*":
            ans = q1 * q2

        else:
            ans = q1 / q2

        try:
            if times > 0:
                root.bind('<Return>', qAnswer)
                askL = Label(text="Whats " + str(q1) + " " + str(op) + " " + str(q2) + "?")
                qStart = time.time()
                times -= 1
                askE = Entry(root)
                askB = Button(text="Done", command=qAnswer)
                askL.grid(row=0, column=0)
                askE.grid(row=1, column=0)
                askB.grid(row=2, column=0)
                break
            else:
                totalTime = time.time() - tStart
                avTime = round((totalTime / timesFinal) - timesFinal, 2)
                endL = Label(text="Finished, you got " + str(correct) + " \nquestions right out of " + str(
                    timesFinal) + " questions.\nYour average  time was " + str(avTime) + " seconds!")

                endB = Button(text="End", command=end, padx=10)
                restartB = Button(text="Restart", command=restart)

                endB.grid(row=1, column=0)
                restartB.grid(row=1, column=1)
                endL.grid(row=0, column=0, columnspan=2)
                break

        except ValueError:
            print("That is not a number")
            clear()
            qGen()


def start():
    welcomeL = Label(text="Welcome to Math Trainer,\nwhat do you want to practice?")
    addB = Button(root, text="+", command=addOp, padx=12)
    subB = Button(root, text="-", command=subOp, padx=12)
    multB = Button(root, text="*", command=multOp, padx=12)
    divB = Button(root, text="/", command=divOp, padx=12)

    welcomeL.grid(row=0, column=0, columnspan=4)
    addB.grid(row=1, column=0)
    subB.grid(row=1, column=1)
    divB.grid(row=1, column=2)
    multB.grid(row=1, column=3)

start()

root.mainloop()
