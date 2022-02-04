#!/usr/bin/env python3
import random

def infloop():
    a = input("Enter the first number of the range that you want the number generator to generate: ")
    b = input("Enter the second number of the range that you want the number generator to generate: ")
    try:
        print('Here is your random number from',a,'to',b,":",(random.randint(int(a), int(b))))
    except ValueError:
        print("Variable(s) contained non-integers!\n")
        infloop()
    c = input(("Would you like to generate another random number? (y/n)\n"))
    if c == ("y" or "yes"):
        infloop()
    elif c == ("n" or "no" or "exit" or "quit" or "q"):
        exit()

infloop()
