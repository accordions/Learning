print("This game will help you determine what's an effective response if you're jumped.")
input("Press enter to continue...")

userInput = input("What distance would you be fighting from? A)Long Distance B)Medium Distance C)Short Distance D)Transition E)On the Ground [A/B/C/D/E]? : ")

#options = ["A","B","C","D","E"]

martialArts = userInput.upper()

while(True):

    if martialArts == 'A':
        print("Kendo, Taekwondo")
        break
    elif martialArts == 'B':
        print("Aikido")
        break
    elif martialArts == 'C':
        print("K1, Jiu Jitsu")
        break
    elif martialArts == 'D':
        print("Judo, Salat, wrestling")
        break
    elif martialArts == 'E':
        print("Brazilian Jiu Jitsu")
        break
    else:
        print("Invalid command.")
        userInput = input("What distance would you be fighting from? A)Long Distance B)Medium Distance C)Short Distance D)Transition E)On the Ground [A/B/C/D/E]? : ")
        martialArts = userInput.upper()

