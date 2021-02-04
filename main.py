import random
import time

dif = 0
times = 0
op = 0

opCheck = True
while opCheck:
    op = (input("Welcome to math trainer, what do you want to practice (+, -, * or /) "))

    if op != "+" and op != "-" and op != "*" and op != "/":
        print("That is not an option")

    else:
        opCheck = False

difCheck = True
while difCheck:
    dif = (input("What difficulty do you want to train at? (Easy Medium or Hard) "))

    if dif.lower() != "easy" and dif.lower() != "medium" and dif.lower() != "hard":
        print("That is not an option")

    else:
        difCheck = False

if dif.lower() == "easy":
    difN = [1, 20]

elif dif.lower() == "medium":
    difN = [1, 50]

else:
    difN = [1, 100]

qCount = True
while qCount:
    try:
        times = int(input("How many questions do you want? "))
        qCount = False

    except ValueError:
        print("That is not a number")
        continue

timesFinal = times
correct = 0

training = True
tStart = time.time()
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
            start = time.time()
            pans = int(input("Whats " + str(q1) + " " + str(op) + " " + str(q2) + "? "))
            times -= 1
        else:
            tEnd = time.time()
            totalTime = tEnd - tStart
            avTime = round(totalTime / timesFinal, 2)
            print("Finished, you got", str(correct), "questions right out of", str(timesFinal), "questions.\nYour average time was", avTime, "seconds!")
            break

    except ValueError:
        print("That is not a number")
        continue

    else:
        if int(pans) == ans:
            end = time.time()
            qTime = round((end - start), 2)
            print("Correct! that took " + str(qTime), "seconds")
            correct += 1

        else:
            print("Failed")
