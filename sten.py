from ast import Compare
from asyncore import loop
import random
list = ["sten", "sax", "påse"]
anwsers2 = ["facebook mamma", "denna kåd är based", "Pojke", "linus L skulle inte ha fåt en tie", "inte ett agel moment", ""]
svar = input("Välkommen, vill du spela ett spel av sten sax påse Y/N?")
while svar.lower == "y":
    horny = input("Välj Sten, sax eller påse")
    einstein = random.choice(list)
    if horny == einstein:
        print (random.choice(anwsers2))
    elif horny == "sten" and einstein == "sax" or horny == "påse" and einstein == "sten" or horny == "sax" and einstein == "påse":
        print()
    else:
        print()
        input("play again? Y/N")
        if 



















#war-kilroy 1945