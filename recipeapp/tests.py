"""Sample tests"""

from django.test import SimpleTestCase

from recipeapp import calc


class CaclTest(SimpleTestCase):
    def test_add_numbers(self):
        """Test adding numbers"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(15, 6)

        self.assertEqual(res, 9)
