import unittest

def is_leap_year(year):
    return (year%4==0 and (year%100!=0 or year%400==0))

class TestLeapYear(unittest.TestCase):
    def test_400_leap_year(self):
        self.assertEqual(True, is_leap_year(400)) 

    def test_300_leap_year(self):
        self.assertEqual(False, is_leap_year(300)) 

    def test_4_leap_year(self):
        self.assertEqual(True, is_leap_year(4)) 

    def test_5_leap_year(self):
        self.assertEqual(False, is_leap_year(5)) 