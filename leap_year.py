import unittest

# Demorgan's law...    
# (x%4==0 and (x%100!=0 or x%400=0))
# (~a and (b or ~c))
# (~a and ~(~b and c))
# ~(a or (~b and c))

f = lambda x: (x%4 or x%100<1 and x%400)<1

class TestLeapYear(unittest.TestCase):
    def test_400_leap_year(self):
        self.assertEqual(True, f(400)) 

    def test_300_leap_year(self):
        self.assertEqual(False, f(300)) 

    def test_4_leap_year(self):
        self.assertEqual(True, f(4)) 

    def test_5_leap_year(self):
        self.assertEqual(False, f(5)) 