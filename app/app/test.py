"""
Sample Test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """ Test the calculator """

    def test_add(self):
        """ Test that two numbers are added together """
        self.assertEqual(calc.add(3, 8), 11)
    def test_subtract(self):
        """ Test that two numbers are subtracted """
        self.assertEqual(calc.subtract(5, 11), 6)