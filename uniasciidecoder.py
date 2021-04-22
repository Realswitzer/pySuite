#!/usr/bin/env python3
def infloop():
    lol = int(input("Insert Unicode/Ascii value: "))
    print("Value: {} Character: {}".format(lol,chr(lol)))
    infloop()
infloop()
