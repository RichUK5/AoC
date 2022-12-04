with open('2022-02-0-input.txt', 'r') as file:
    InputData = file.read()
InputList = list(filter(None, InputData.split("\n")))

import unittest

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

pt2
X lose
Y draw
Z win
"""

class Game(object):
    Score = 0

    # The class "constructor" - It's actually an initializer 
    def __init__(self, GameString):
        game = GameString.split(" ")
        match game[1]:
            case "X":
                self.Score += 0
                match game[0]:
                    case "A":
                        self.Score += 3
                    case "B":
                        self.Score += 1
                    case "C":
                        self.Score += 2
            case "Y":
                self.Score += 3
                match game[0]:
                    case "A":
                        self.Score += 1
                    case "B":
                        self.Score += 2
                    case "C":
                        self.Score += 3
            case "Z":
                self.Score += 6
                match game[0]:
                    case "A":
                        self.Score += 2
                    case "B":
                        self.Score += 3
                    case "C":
                        self.Score += 1

def Make_Game(GameString):
    game = Game(GameString)
    return game


class TestGame(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4,Make_Game("A Y").Score)
    def test_2(self):
        self.assertEqual(1,Make_Game("B X").Score)
    def test_3(self):
        self.assertEqual(7,Make_Game("C Z").Score)
        #self.assertEqual(15,Game(["A Y","B X","C Z"]).Score)

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestGame))

Games = []
for NewGame in InputList:
    Games.append(Make_Game(NewGame))

print(sum(Game.Score for Game in Games))