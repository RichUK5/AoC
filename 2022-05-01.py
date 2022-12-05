import unittest

class Stack:
    Name = ""
    Crates = []

    def __init__(self, Name):
        self.Name = Name
        self.Crates = []

def Make_Stack(Name):
    stack = Stack(Name)
    return stack

def SplitBlocks(String):
    return list(filter(None, String.split("\n\n")))

def MakeStacks(List):
    Stacks = []
    for Item in List:
        Stacks.append(Make_Stack(Item))
    return Stacks

def PlaceCrates(String):
    StacksLines = String.splitlines()
    StacksLines.reverse()
    Stacks = MakeStacks(StacksLines[0][1::4])
    for Line in StacksLines[1:]:
        for Column, Crate in enumerate(Line[1::4]):
            if Crate != " ":
                Stacks[Column].Crates.append(Crate)
    return Stacks

def GetStack(String, Stacks):
    for Stack in Stacks:
        if Stack.Name == String:
            return Stack

def MoveCrates(Stacks, InstructionsString):
    Instructions = InstructionsString.splitlines()
    for Instruction in Instructions:
        QtyString, Src, Dst = Instruction.split(" ")[1::2]
        Qty = int(QtyString)
        SrcStack = GetStack(Src,Stacks)
        DstStack = GetStack(Dst,Stacks)
        while Qty > 0:
            Qty = Qty - 1
            DstStack.Crates.append(SrcStack.Crates.pop())

def Part1(String):
    StacksString, InstructionsString = SplitBlocks(String)
    Stacks = PlaceCrates(StacksString)
    MoveCrates(Stacks, InstructionsString)
    return "".join([o.Crates[-1] for o in Stacks])
        

with open('2022-05-0-test.txt', 'r') as file:
    TestData = file.read()
with open('2022-05-0-input.txt', 'r') as file:
    InputData = file.read()

class Test(unittest.TestCase):
    def test_Part1_1(self):
        self.assertEqual('CMZ',Part1(TestData))

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(Test))

print(Part1(InputData))