from Player import Player
import Data


class ScoreBoard:
    players = []


    def __init__(self, players):
        self.players = players
        self.printScoreBoard()


    def printScoreBoard(self):
        if self.players is None:
            return 0 
        for player in self.players:
            print(player.getName() + (" " * (12 - len(player.getName()))) + "| " + chr(0x2588) * player.getScore())


#def main():
    #players = [Player("Daniel", "SE", [], "", 1), Player("Dan", "SE", [], "", 5), Player("Daniel", "SE", [], "", 10)]
    #ScoreBoard(players).printScoreBoard()

#main()