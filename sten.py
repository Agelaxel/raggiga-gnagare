import random
import time

poängspelare = 0
poängdator = 0
list = ["sten", "sax", "påse"]
answers2 = ["facebook mamma", "denna kod är based", "Pojke", "linus L skulle inte ha fått en tie", "inte ett agel moment"
, "egg"]
svar = input("Välkommen, vill du spela ett spel av sten sax påse [Y]/[n]?\n")

while svar.lower() != "n":
    spelarval = input("Välj Sten, sax eller påse:\n")
    spelarval = spelarval.lower()
    datorval = random.choice(list)
    if spelarval == datorval:
        print(random.choice(answers2))
    elif spelarval == "sten" and datorval == "sax" or spelarval == "påse" and datorval == "sten" or spelarval == "sax" and datorval == "påse":
        print("\nDu vann :D")
        poängspelare = poängspelare+1
        print(f'du har: {poängspelare} poäng :D\n')
    else:
        print("\ndu FÖRLORA >:))))")
        poängdator = poängdator+1
        print(f'DATORN har: {poängdator} poäng >:)\n')

    if poängspelare >= 2:
        print("DU VANN :DDDD stiligt")
        time.sleep(1)
        igen = input("ska vi spela igen!? [Y]/[N]\n")
        if igen.lower() == "y":
            print("okidoki! :D")
            poängdator = 0
            poängspelare = 0
        if igen.lower() == "n":
            print("Noobium.")
            exit()
#egg
    if poängdator >= 2:
        print("DATORN vann >:) (noobium)")
        time.sleep(1)
        igen = input("ska vi spela igen!? [Y]/[N]\n")
        if igen.lower() == "y":
            print("okidoki! :D")
            poängdator = 0
            poängspelare = 0
        if igen.lower() == "n":
            print("Noobium.")
            exit()
    


















#war-kilroy 1945