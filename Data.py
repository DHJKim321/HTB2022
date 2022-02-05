import random

class gameState():

    players = []
    completePlayers = []
    round = 0

    def addPlayer(self,player):
        self.players.append(player)
        self.completePlayers.append(player)
    def getPlayers(self):
        return self.players
    def nextRound(self):
        self.round += 1
    def getRound(self):
        return round
    def getRandPlayer(self):
        self.players.pop(random.choice(self.players))
