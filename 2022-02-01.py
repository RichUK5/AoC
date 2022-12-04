with open('2022-02-0-input.txt', 'r') as file:
    InputData = file.read()
InputList = list(filter(None, InputData.split("\n")))

"""
Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.

The first column is what your opponent is going to play:
A for Rock
B for Paper
C for Scissors

The second column, you reason, must be what you should play in response:
X for Rock
Y for Paper
Z for Scissors

1 for Rock, 2 for Paper, and 3 for Scissors
0 if you lost, 3 if the round was a draw, and 6 if you won

X draws A
X loses B
X wins C

Y wins A
Y draws B
Y loses C

Z loses A
Z wins B
Z draws C
"""

class Game(object):
    Score = 0

    # The class "constructor" - It's actually an initializer 
    def __init__(self, GameString):
        game = GameString.split(" ")
        match game[1]:
            case "X":
                self.Score += 1
                if game[0] == "A":
                    self.Score += 3
                elif game[0] == "C":
                    self.Score += 6
            case "Y":
                self.Score += 2
                if game[0] == "B":
                    self.Score += 3
                elif game[0] == "A":
                    self.Score += 6
            case "Z":
                self.Score += 3
                if game[0] == "C":
                    self.Score += 3
                elif game[0] == "B":
                    self.Score += 6

def Make_Game(GameString):
    game = Game(GameString)
    return game


Games = []
for NewGame in InputList:
    Games.append(Make_Game(NewGame))

print(sum(Game.Score for Game in Games))