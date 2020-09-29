import unittest
from programer import Programer

class ProgramerTestcase(unittest.TestCase):

    def setUp(self):
        self.original_salay = 10000
        self.programer = Programer('Becky',34,self.original_salay)

    def test_default_raise(self):
        """default raise salary"""
        self.programer.give_raise()
        self.assertEqual(self.programer.salary,self.original_salay+5000)

    def test_given_raise(self):
        """given salary raise"""
        increase_salary = 8000
        self.programer.give_raise(increase_salary)
        self.assertEqual(self.programer.salary,self.original_salay+increase_salary)


if __name__ == '__main__':
        unittest.main()
