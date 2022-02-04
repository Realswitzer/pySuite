import random
from random import randrange

while True :
    a = int(input("Enter the first number of the range that you want the number generator to generate: "))
    b = int(input("Enter the second number of the range that you want the number generator to generate: "))
    c = 0
    
    while c < 1:
        print('Here is your random number from',a,'to',b,":",(randrange(a, b)))
        c += 1

    print("Would you like to generate another random number? (y/n) (You might have to type it a few times for some reason, if you can fix it in the code, please do and submit a pull request. Thanks.)")
    input()
    if input() == "y":
        False
    if input() == "n":
        break