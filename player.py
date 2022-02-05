class Player:
    name = ""
    title = ""
    false_list = []
    true_title = ""
    score = 0

    def __init__(self, name, title, false_list, true_title, score):
        self.name = name
        self.title = title
        self.false_list = false_list
        self.true_title = true_title
        self.score = score


    def __str__(self):
        return ("Name: " + self.name + "\n" + "Job title: " + self.title + "\n" + 
                "Choices: " + self.false_list[0] + ", " + self.false_list[1] + ", " + self.true_title )

    
    def setName(self):
        self.name = input("Enter your name: ")


    def getName(self):
        return self.name


    def setTitle(self):
        self.title = input("Enter your current job title")


    def getTitle(self):
        return self.title


    def addScore(self, score):
        self.score += score

    
    def getScore(self):
        return self.score


    def setFalses(self):
        false_1 = input("Enter one false AND title: ")
        false_2 = input("Enter another false AND title: ")
        self.false_list.append(false_1)
        self.false_list.append(false_2)


    def getFirstFalse(self):
        return self.false_list[0]

    
    def getSecondFalse(self):
        return self.false_list[1]


    def setTrueTitle(self):
        true_title = input("Enter your actual AND title: ")
        self.true_title = true_title


    def getTrueTitle(self):
        return self.true_title


def main():
    player1 = Player("Daniel Kim", "Software Engineer", ["Gamer", "Musician"], "Gardener", 0)
    print(player1)
main()
    