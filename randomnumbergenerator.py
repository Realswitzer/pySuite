import random

def infloop():
    a = int(input("Enter the first number of the range that you want the number generator to generate: "))
    b = int(input("Enter the second number of the range that you want the number generator to generate: "))

    print('Here is your random number from',a,'to',b,":",(random.randint(a, b)))
    print("Would you like to generate another random number? (y/n)\n")
    c = str(input())
    print()
    if c == "y":
        infloop()
    elif c == "n":
        exit()

infloop()
