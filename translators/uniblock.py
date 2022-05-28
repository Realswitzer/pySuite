#!/usr/bin/env python3

# Improved Python version of the block translator!
# Original: https://lingojam.com/%E2%96%88%E2%96%88%E2%96%88%E2%96%88translator
# Fixes problem of random inserted spaces making decoding finnicky.
# Thanks Gaia for making me unintentionally make this.
# Yeah, okay I think that's enough monologuing. -switz

def main():
    print("Encode = 1 | Decode = 2")
    try:
        mode = int(input("What mode should the translator run in? (1/2): "))
    except ValueError:
        print("Mode was set to an invalid value! Aborting.")
        exit()
    if mode == 1:
        message = str(input("insert original message: "))
        message = message.lower()

        message = message.replace("a", "▀")
        message = message.replace("b", "▁")
        message = message.replace("c", "▂")
        message = message.replace("d", "▃")
        message = message.replace("e", "▄")
        message = message.replace("f", "▅")
        message = message.replace("g", "▆")
        message = message.replace("h", "▇")
        message = message.replace("i", "█")
        message = message.replace("j", "▉")
        message = message.replace("k", "▊")
        message = message.replace("l", "▋")
        message = message.replace("m", "▌")
        message = message.replace("n", "▍")
        message = message.replace("o", "▎")
        message = message.replace("p", "▏")
        message = message.replace("q", "▐")
        message = message.replace("r", "░")
        message = message.replace("s", "▒")
        message = message.replace("t", "▔")
        message = message.replace("u", "▕")
        message = message.replace("v", "▙")
        message = message.replace("w", "▚")
        message = message.replace("x", "▛")
        message = message.replace("y", "▜")
        message = message.replace("z", "▟")

        print(" " + message)

        check = input(("Would you like to translate more? (y/n)\n"))
        if check == ("y" or "yes"):
            main()
        elif check == ("n" or "no" or "exit" or "quit" or "q"):
            exit()

    elif mode == 2:
        message = str(input("insert encoded message: "))
        message = message.lower()

        message = message.replace("▀", "a")
        message = message.replace("▁", "b")
        message = message.replace("▂", "c")
        message = message.replace("▃", "d")
        message = message.replace("▄", "e")
        message = message.replace("▅", "f")
        message = message.replace("▆", "g")
        message = message.replace("▇", "h")
        message = message.replace("█", "i")
        message = message.replace("▉", "j")
        message = message.replace("▊", "k")
        message = message.replace("▋", "l")
        message = message.replace("▌", "m")
        message = message.replace("▍", "n")
        message = message.replace("▎", "o")
        message = message.replace("▏", "p")
        message = message.replace("▐", "q")
        message = message.replace("░", "r")
        message = message.replace("▒", "s")
        message = message.replace("▔", "t")
        message = message.replace("▕", "u")
        message = message.replace("▙", "v")
        message = message.replace("▚", "w")
        message = message.replace("▛", "x")
        message = message.replace("▜", "y")
        message = message.replace("▟", "z")

        print(" " + message)

        check = input(("Would you like to translate more? (y/n)\n"))
        if check == ("y" or "yes"):
            main()
        elif check == ("n" or "no" or "exit" or "quit" or "q"):
            exit()

if __name__ == "__main__":
    main()
