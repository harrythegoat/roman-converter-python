import unittest
from romanController import romanConverter
roman = romanConverter()

class TestRomanConverter(unittest.TestCase):
    def testRomanToInt(self):
        self.assertEqual(roman.romanInteger("我是一只小小鸟"), "Invalid roman value.")
        self.assertEqual(roman.romanInteger("A"), "Invalid roman value.")
        self.assertEqual(roman.romanInteger("MMMMMMMMMM"), "Maximum roman value is 3999.")
        self.assertEqual(roman.romanInteger(1995), "Value must be string.")
        self.assertEqual(roman.romanInteger(""), "Value cannot be empty.")
        self.assertEqual(roman.romanInteger(None), "Value must be string.")
    
    def testIntToRoman(self):
        self.assertEqual(roman.integerRoman("ILoveKFC"), "Invalid value.")
        self.assertEqual(roman.integerRoman("!@#!%!@#"), "Invalid value.")
        self.assertEqual(roman.integerRoman("我是一只小小鸟"), "Invalid value.")
        self.assertEqual(roman.integerRoman(4000), "Value must be in range of 0 - 3999.")
        self.assertEqual(roman.integerRoman(0), "Value must be in range of 0 - 3999.")
        self.assertEqual(roman.integerRoman(""), "Invalid value.")
        self.assertEqual(roman.integerRoman(None), "Value must be Integer.")

if __name__ == '__main__':
    unittest.main()