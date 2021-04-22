import codecs

def infloop():
    passrot13 = lambda s : codecs.getencoder("rot-13")(s)[0]
    print("NOTE: Encoding a ROT13 string will decode it.")
    thestring = str(input("What string do you want to ROT13 encode? "))
    print(rot13(thestring))
    infloop()
infloop()
