# tests/test_functions.py
import unittest
from src.example.functions import times, divide

class TestFunctions(unittest.TestCase):
    def test_times(self):
        self.assertEqual(times(2, 3), 6)
        self.assertEqual(times(-1, 1), -1)
    def test_divide(self):
	self.assertEqual(divide(8, 2), 4)
	self.asserrEqual(divide(0, 7), 0)

if __name__ == '__main__':
    unittest.main()
