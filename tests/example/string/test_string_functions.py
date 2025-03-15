# tests/example/string/test_string_functions.py

import unittest
from src.example.string import reverse

class TestStringFunctions(unittest.TestCase):
    def test_reverse(self):
        print("test reverse...")
        self.assertEqual(reverse('abcd'), 'dcba')        

if __name__ == '__main__':
    unittest.main()
