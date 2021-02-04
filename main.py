import random
import time

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
    difn = [1, 20]

elif dif.lower() == "medium":
    difn = [1, 50]

else:
    difn = [1, 100]

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

while training:
    q1 = (random.randint(difn[0], difn[1]))
    q2 = (random.randint(difn[0], difn[1]))

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
            print("Finished, you got", str(correct), "questions right out of", str(timesFinal), "questions")
            break

    except ValueError:
        print("That is not a number")
        continue

    else:
        if int(pans) == ans:
            end = time.time()
            totalTime = round((end - start), 2)
            print("Correct! that took " + str(totalTime), "seconds")
            correct += 1

        else:
            print("Failed")

