import random

class gameState():

    players = []
    completePlayers = []
    round = 0

    def addPlayer(self,player):
        self.players.append(player)
        self.completePlayers.append(player)

    def getPlayers(self):
        if self.players == []:
            return None
        return self.players

    def getCompletePlayers(self):
        if self.completePlayers == []:
            return None
        return self.completePlayers

    def nextRound(self):
        self.round += 1

    def getRound(self):
        return round

    def getRandPlayer(self):
        if self.players != []:
            choice = random.choice(self.players)
            self.players.remove(choice)
            return choice
        return None
