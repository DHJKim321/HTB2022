# HTB2022

AND Challenge:
    Two falses one truth - Either: One person, three titles OR three pairs of people

Domain name: andatruth.tech
Username: dhjkim200178384
Password: WelcomeToHTB08!
Who is your favourite historical character: Jesus Christ



Overview: Game chooses a user at random. User inputs two false AND titles and one true. Everyone else chooses what the two falses and one true ones are.

Game starts
Everyone inputs: 
    Take photo with webcam
    Name: Daniel Kim
    Job title: Software Engineer
    False #1: Gamer
    False #2: Gardener
    True: Musician

Game chooses someone
Everyone else is presented with False #1, #2, True
Everyone chooses which ones are false and true
Calculate score based on time taken/number of correct guesses (Low priority)

Necessary files:
    Player class:
        Constructor
        Get name
        Get Job title
        Get score
        Add score
        Get 2 false and 1 true AND titles
        Get photo (Not yet)
        Pretty print
    Game controller class:
        Start game
        Control game flow
    Scoreboard class:
        Pretty print scoreboard
