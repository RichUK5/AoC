import unittest

def SplitLines(String):
    return list(filter(None, String.split("\n")))

def FullyContains(String):
    Assignments = String.split(",")
    Assignment1 = list(map(int, Assignments[0].split("-")))
    Assignment2 = list(map(int, Assignments[1].split("-")))
    
    if   Assignment1[0] >= Assignment2[0] and Assignment1[1] <= Assignment2[1]: return True
    elif Assignment1[0] <= Assignment2[0] and Assignment1[1] >= Assignment2[1]: return True
    else: return False

def PartiallyContains(String):
    Assignments = String.split(",")
    Assignment1 = list(map(int, Assignments[0].split("-")))
    Assignment2 = list(map(int, Assignments[1].split("-")))
    
    if   Assignment1[1] >= Assignment2[0] and Assignment1[0] <= Assignment2[1]: return True
    elif Assignment1[0] >= Assignment2[1] and Assignment1[1] <= Assignment2[0]: return True
    else: return False
    
def TotalFullyContains(List):
    Total = 0
    for Item in List:
        if FullyContains(Item) == True: Total += 1
    return Total

def TotalPartiallyContains(List):
    Total = 0
    for Item in List:
        if PartiallyContains(Item) == True: Total += 1
    return Total
        

class Test(unittest.TestCase):
    def test_SplitLines_1(self):
        self.assertEqual(['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8'],SplitLines(TestData))
    def test_FullyContains_1(self):
        self.assertFalse(FullyContains('2-4,6-8'))
    def test_FullyContains_2(self):
        self.assertFalse(FullyContains('2-3,4-5'))
    def test_FullyContains_3(self):
        self.assertFalse(FullyContains('5-7,7-9'))
    def test_FullyContains_4(self):
        self.assertTrue(FullyContains('2-8,3-7'))
    def test_FullyContains_5(self):
        self.assertTrue(FullyContains('6-6,4-6'))
    def test_FullyContains_6(self):
        self.assertFalse(FullyContains('2-6,4-8'))
    def test_TotalFullyContains_1(self):
        self.assertEqual(2,TotalFullyContains(SplitLines(TestData)))
    def test_PartiallyContains_1(self):
        self.assertFalse(PartiallyContains('2-4,6-8'))
    def test_PartiallyContains_2(self):
        self.assertFalse(PartiallyContains('2-3,4-5'))
    def test_PartiallyContains_3(self):
        self.assertTrue(PartiallyContains('5-7,7-9'))
    def test_PartiallyContains_4(self):
        self.assertTrue(PartiallyContains('2-8,3-7'))
    def test_PartiallyContains_5(self):
        self.assertTrue(PartiallyContains('6-6,4-6'))
    def test_PartiallyContains_6(self):
        self.assertTrue(PartiallyContains('2-6,4-8'))
    def test_TotalPartiallyContains_1(self):
        self.assertEqual(4,TotalPartiallyContains(SplitLines(TestData)))

TestData = """2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8"""
TestList = SplitLines(TestData)

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(Test))

with open('2022-04-0-input.txt', 'r') as file:
    InputData = file.read()
print(TotalFullyContains(SplitLines(InputData)))
print(TotalPartiallyContains(SplitLines(InputData)))