import unittest
from unittest import TestCase
from parenthesis import p_balance

class Test_p_balance(TestCase):

    @classmethod
    def setUp(self) -> None:
        print('setUp')

    @classmethod
    def tearDown(self) -> None:
        print('tearDown')

    def test_p_balance_balance(self):
        self.assertEqual(p_balance('[([])((([[[]]])))]{()}'),"Сбалансированно")

    def test_p_balance_unbalance(self):
        self.assertEqual(p_balance('((}{[]}}}]])))(((([}[{}}]{])()()'),"Несбалансированно")

