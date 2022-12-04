with open('2022-01-0-input.txt', 'r') as file:
    InputData = file.read()

class Elf(object):
    Foods = []
    TotalCalories = 0

    # The class "constructor" - It's actually an initializer 
    def __init__(self, FoodString):
        FoodArray = FoodString.split("\n")
        self.Foods = [int(numeric_string) for numeric_string in FoodArray]
        self.TotalCalories = sum(self.Foods)

def Make_Elf(FoodsString):
    elf = Elf(FoodsString)
    return elf

ElvesInput = list(filter(None, InputData.split("\n\n")))
Elves = []
for NewElfInput in ElvesInput:
    Elves.append(Make_Elf(NewElfInput))

Elves.sort(key=lambda x: x.TotalCalories, reverse=True)
print(Elves[0].TotalCalories + Elves[1].TotalCalories + Elves[2].TotalCalories)