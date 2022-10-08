import unittest
from Calc import Calculator

#Tests
class TestCalc(unittest.TestCase):

    def test_add(self):
        x = Calculator.add(5,5)
        self.assertEqual(x,10)

    def test_sub(self):
        x = Calculator.sub(10,5)
        self.assertEqual(x,5)
        
    def test_mult(self):
        x = Calculator.mult(5,2)
        self.assertEqual(x,10)

    def test_div(self):
        x = Calculator.div(10,2)
        self.assertEqual(x,5)

    def test_null(self):
        self.assertIsNotNone(a, "a can't be null")
        self.assertIsNotNone(a, "b can't be null")


class Main:
    
    #Getting inputs
    def getab():
        global a,b

        a = input("Give a:")
        b = input("Give b:")

        if a == "" or b == "":
            raise ValueError("!a and b can't be null!")

        a = int(a)
        b = int(b)

    #Choosing operation
    def operation():
        qwe = input("Choose operation[+|-|*|/]:")

        if qwe == "+":
            Calculator.add(a,b)
        elif qwe == "-":
            Calculator.sub(a,b)
        elif qwe == "*":
            Calculator.mult(a,b)
        elif qwe == "/":
            Calculator.div(a,b)

    #Testing
    def doTests():
        asd = input("Would you like to test Calculator? [y/n]:").lower()
        if asd == "y":
            unittest.main()
        else:
            pass

#Engaging functions
Main.getab()
Main.operation()
Main.doTests()