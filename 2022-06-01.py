import unittest

def Part1(String):
    pos = 4
    i = 0
    Array = [*String[0:3]]
    for Char in String[3:]:
        if len(set(Array)) == len(Array):
            if Char not in Array:
                return pos
        if i == 3:
            i = 0
        Array[i] = Char
        pos += 1
        i += 1
    return -1
        
with open('2022-06-0-test1.txt', 'r') as file:
    TestData1 = file.read()
with open('2022-06-0-test2.txt', 'r') as file:
    TestData2 = file.read()
with open('2022-06-0-test3.txt', 'r') as file:
    TestData3 = file.read()
with open('2022-06-0-test4.txt', 'r') as file:
    TestData4 = file.read()
with open('2022-06-0-test5.txt', 'r') as file:
    TestData5 = file.read()
with open('2022-06-0-input.txt', 'r') as file:
    InputData = file.read()

class Test(unittest.TestCase):
    def test_Part1_1(self):
        self.assertEqual(7,Part1(TestData1))
    def test_Part1_2(self):
        self.assertEqual(5,Part1(TestData2))
    def test_Part1_3(self):
        self.assertEqual(6,Part1(TestData3))
    def test_Part1_4(self):
        self.assertEqual(10,Part1(TestData4))
    def test_Part1_5(self):
        self.assertEqual(11,Part1(TestData5))

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(Test))

print(Part1(InputData))