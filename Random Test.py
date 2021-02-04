import random

active = (input("Do you want to generate an int? (y or n) "))

while active == "y":
    n1 = (input("Between number 1 "))
    n2 = (input("Between number 2 "))
    print(random.randint(int(n1), int(n2)))
    active = (input("Do you want to generate another int? (y or n) "))