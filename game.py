
import player
import Data


data = Data()

def startGame():
    print("the active players are:")

    for player in data.getPlayers():
        if player is not None:
            print(f"{player.getName()}\n", 20)



    response = input("Do you want to add another player?").tolower()

    while response == "y":
        newPlayer = player
        data.addPlayer(newPlayer)
        response = input("Do you want to add another player?").tolower()
    playRound()


def playRound():
    data.getRandPlayer()

    






startGame()
