import random

def infloop():
    try:
        a = int(input("Enter the first number of the range that you want the number generator to generate: "))
    except:
        print("Variable a attempted to be set to a non-integer character!")
        print()
        infloop()
    try:
        b = int(input("Enter the second number of the range that you want the number generator to generate: "))
    except:
        print("Variable b attempted to be set to a non-integer character!")
        print()
        infloop()
    print('Here is your random number from',a,'to',b,":",(random.randint(a, b)))
    print("Would you like to generate another random number? (y/n)\n")
    c = str(input())
    if c == "y":
        infloop()
    elif c == "n":
        exit()
infloop()
