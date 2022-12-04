with open('2022-03-0-input.txt', 'r') as file:
    InputData = file.read()
InputList = list(filter(None, InputData.split("\n")))
import unittest

"""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""



def SplitString(String):
    halfway = int(len(String)/2)
    return String[:halfway], String[halfway:]

def FindMatchingChar(strings):
    for char in strings[0]:
        if char in strings[1]:
            return char

def ConvertChar(char):
    priority = ord(char)
    if priority > 96:
        priority -= 96
    else:
        priority -= 38
    return priority

def TotalPriorities(List):
    Total = 0
    for item in List:
        Total += ConvertChar(FindMatchingChar(SplitString(item)))
    return Total

def FindMatchingBadge(strings):
    for char in strings[0]:
        if char in strings[1]:
            if char in strings[2]:
                return char

def TotalBadgePriorities(List):
    Total = 0
    for i in range(0, len(List), 3):
        Total += ConvertChar(FindMatchingBadge([List[i],List[i+1],List[i+2]]))
    return Total


# The sum of these is 70.

class Test(unittest.TestCase):
    def test_SplitString_1(self):
        self.assertEqual(("vJrwpWtwJgWr","hcsFMMfFFhFp"),SplitString("vJrwpWtwJgWrhcsFMMfFFhFp"))
    def test_SplitString_2(self):
        self.assertEqual(("jqHRNqRjqzjGDLGL","rsFMfFZSrLrFZsSL"),SplitString("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"))
    def test_SplitString_2(self):
        self.assertEqual(("PmmdzqPrV","vPwwTWBwg"),SplitString("PmmdzqPrVvPwwTWBwg"))
    def test_ConvertChar_1(self):
        self.assertEqual(16,ConvertChar("p"))
    def test_ConvertChar_1(self):
        self.assertEqual(38,ConvertChar("L"))
    def test_ConvertChar_2(self):
        self.assertEqual(42,ConvertChar("P"))
    def test_ConvertChar_3(self):
        self.assertEqual(22,ConvertChar("v"))
    def test_ConvertChar_4(self):
        self.assertEqual(20,ConvertChar("t"))
    def test_ConvertChar_5(self):
        self.assertEqual(19,ConvertChar("s"))
    def test_FindMatchingChar_1(self):
        self.assertEqual('p',FindMatchingChar(["vJrwpWtwJgWr","hcsFMMfFFhFp"]))
    def test_FindMatchingChar_1(self):
        self.assertEqual('L',FindMatchingChar(("jqHRNqRjqzjGDLGL","rsFMfFZSrLrFZsSL")))
    def test_FindMatchingChar_1(self):
        self.assertEqual('P',FindMatchingChar(("PmmdzqPrV","vPwwTWBwg")))
    def test_All_1(self):
        self.assertEqual(16,ConvertChar(FindMatchingChar(SplitString("vJrwpWtwJgWrhcsFMMfFFhFp"))))
    def test_All_2(self):
        self.assertEqual(38,ConvertChar(FindMatchingChar(SplitString("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"))))
    def test_All_3(self):
        self.assertEqual(42,ConvertChar(FindMatchingChar(SplitString("PmmdzqPrVvPwwTWBwg"))))
    def test_All_4(self):
        self.assertEqual(22,ConvertChar(FindMatchingChar(SplitString("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn"))))
    def test_All_5(self):
        self.assertEqual(20,ConvertChar(FindMatchingChar(SplitString("ttgJtRGJQctTZtZT"))))
    def test_All_6(self):
        self.assertEqual(19,ConvertChar(FindMatchingChar(SplitString("CrZsJsPPZsGzwwsLwLmpwMDw"))))
    def test_TotalPriorities_1(self):
        self.assertEqual(157,TotalPriorities(['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']))
    def test_FindMatchingBadge_1(self):
        self.assertEqual('r',FindMatchingBadge(("vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg")))
    def test_FindMatchingBadge_2(self):
        self.assertEqual('Z',FindMatchingBadge(("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw")))
    def test_TotalBadgePriorities_1(self):
        self.assertEqual(70,TotalBadgePriorities(['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']))
    

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(Test))


#Total = 0
#Total += ConvertChar(Char)

print("Total Priorities: ", TotalPriorities(InputList))
print("Total Priorities: ", TotalBadgePriorities(InputList))