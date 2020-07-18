from django.test import TestCase

from app.calculations import sum


class CalcTests(TestCase):

    def test_print_sum(self):
        '''Test to return the valid value for sum'''
        self.assertEquals(sum(3, 3), 6)
