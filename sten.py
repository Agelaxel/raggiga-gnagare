import random

poängspelare = 0
poängdator = 0
list = ["sten", "sax", "påse"]
answers2 = ["facebook mamma", "denna kod är based", "Pojke", "linus L skulle inte ha fått en tie", "inte ett agel moment"
, "egg"]
svar = input("Välkommen, vill du spela ett spel av sten sax påse Y/N?")
while svar.lower() == "y":
    horny = input("Välj Sten, sax eller påse:\n")
    horny = horny.lower()
    einstein = random.choice(list)
    if horny == einstein:
        print(random.choice(answers2))
    elif horny == "sten" and einstein == "sax" or horny == "påse" and einstein == "sten" or horny == "sax" and einstein == "påse":
        print("Du vann :D")
        poängspelare = poängspelare+1
        print(f'du har: {poängspelare} poäng :D\n')
    else:
        print("du FÖRLORA >:))))")
        poängdator = poängdator+1
        print(f'DATORN har: {poängdator} poäng >:)\n')
        # input("play again? Y/N")
        # if 
    if poängspelare >= 2:
        print("DU VANN :DDDD stiligt")
        exit()
    if poängdator >= 2:
        print("du förlora >:((( egg")
        exit()
    



















#war-kilroy 1945