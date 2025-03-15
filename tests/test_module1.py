# tests/test_module1.py
import unittest
from src.module1 import add

class TestModule1(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

