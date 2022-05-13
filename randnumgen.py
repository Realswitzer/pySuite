#!/usr/bin/env python3
import random, sys, getopt, platform

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

# I skidded most of the code below. Manually typed, don't know why.
# https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# Enjoy I guess. -swiss cheese

def main(argv):
    a = ''
    b = ''
    try:
        opts, args = getopt.getopt(argv,"hn:x:",["help","min=","max=","headless"])
    except getopt.GetoptError:
        print("I don't know how you triggered the opt error, but here we are. Exiting")
        exit()
    if opts == []:
        print("No arguments! Launching GUI version...because apparently #4 exists")
        if platform.system() == 'Darwin':
            print("Sorry, dearpygui doesn't seem to work on Mac, at least for me (developer).")
            print("I hope that pygame works, but there's no implementation of that.")
            print("Please use --headless (cli gui-thing) or --help for other options. -switz")
            exit(1)
        dpgfunc()
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('Usage: [file name] [args]')
            print('args: ')
            print('')
            print('   -n --min <minimum value>')
            print('   -x --max <maximum value>')
            exit()
        elif opt in ("-n", "--min"):
            a = str(arg)
        elif opt in ("-x", "--max"):
            b = str(arg)
        elif opt == "--headless":
            infloop()
    try:
        print('Here is your random number from',a,'to',b,':',(random.randint(int(a), int(b))))
    except ValueError:
        print("Variable(s) contained non-integers!\n")
        exit()
    exit()


if __name__ == "__main__":
    main(sys.argv[1:])
