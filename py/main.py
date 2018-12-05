from budget import startBudget

def mainPage():

    displayTitle()
    
    print("What would you like to do? ")
    print("Manage budget (1)")

    answer = input("Selection: ")

    if answer == 1:
        startBudget()


def displayTitle():
    l1 = "     ____.       __            .___                   "
    l2 = "    |    |____  |  | __ ____   |   | ____   ____      "
    l3 = "    |    \__  \ |  |/ // __ \  |   |/    \_/ ___\     "
    l4 = "/\__|    |/ __ \|    <\  ___/  |   |   |  \  \___     "
    l5 = "\________(____  /__|_ \\\___  > |___|___|  /\___  > /\ "
    l6 = "              \/     \/    \/           \/     \/  \/ "

    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)

if __name__ == "__main__":
        mainPage()