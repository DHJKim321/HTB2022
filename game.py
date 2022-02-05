
import Player
import Data
gameState = Data.gameState()

def startGame():
    print("the active players are:")

    response = input("Do you want to add another player?").lower()
    print(response)
    while response == "y":

        gameState.addPlayer(buildPlayer())
        response = input("Do you want to add another player?").lower()
    playRound()

def showPlayers():
        for player in gameState.getPlayers():
            if player is not None:
                print(f"{player.getName()}\n")

def playRound():
    showPlayers()
    #gameState.getRandPlayer()


    
def buildPlayer():
    name = input("what is the players name?")
    title = input("what is the players job title?")
    false_1 = input("What is the first false and?")
    false_2 = input("What is the second false and?")
    true_title = input("What is the players real and?")
    return Player.Player(name,title,[false_1,false_2],true_title,0)





startGame()
