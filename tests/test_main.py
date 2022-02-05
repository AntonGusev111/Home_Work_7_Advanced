import unittest
from unittest import TestCase
from main import Stack

class test_main_func(TestCase):

    @classmethod
    def setUp(self) -> None:
        print('setUp')

    @classmethod
    def tearDown(self) -> None:
        print('tearDown')

    def test_is_empty(self):
        self.assertEqual(Stack().isEmpty(),True)

    def test_pop(self):
        self.assertEqual(Stack().pop(),'stak is empty')

    def test_size(self):
        self.assertEqual(Stack().size(),0)


