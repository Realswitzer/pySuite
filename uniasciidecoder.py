#!/usr/bin/env python3
def infloop():
    theinput = input("Insert Unicode/Ascii value: ")
    try:
        theinput = int(theinput)
        print("Value: {} Character: {}".format(theinput,chr(theinput)))
    except ValueError:
        print("Error: ValueError.")
        print("Input was not an integer.")
        infloop()
    else:
        infloop()
infloop()
