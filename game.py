import player

activePlayers = []
pastPlayers = activePlayers

def startGame():
    for player in activePlayers:
        if player is not None:
            print(f"{player.getName()}\n", 20)

        




