
import Player
import Data
from Scoreboard import ScoreBoard
#import Scoreboard
gameState = Data.gameState()
def startGame():

    response = input("Do you want to add another player?").lower()

    while response == "y":
        gameState.addPlayer(buildPlayer())
        response = input("Do you want to add another player?").lower()
    
    playRound()

def showPlayers():
    players = gameState.getCompletePlayers()
    ScoreBoard(players)
    

def playRound():
    print(f"\n The scores on the doors are : \n")
    showPlayers()

    while gameState.getPlayers() is not None:
        choice = gameState.getRandPlayer()
        print(choice)
        if input() != choice.getTrueTitle():
            choice.addScore(1)
            gameState.addPlayerMini(choice)
        

     


    else:
        ScoreBoard(gameState.getCompletePlayers())
        print("Game over")
        


    
def buildPlayer():
    name = input("what is the players name?")
    title = input("what is the players job title?")
    false_1 = input("What is the first false and?")
    false_2 = input("What is the second false and?")
    true_title = input("What is the players real and?")
    return Player.Player(name,title,[false_1,false_2],true_title,0)





startGame()
