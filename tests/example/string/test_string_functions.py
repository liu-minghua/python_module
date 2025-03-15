# tests/example/string/test_string_functions.py

import unittest
from src.example.string.string_functions import reverse

class TestStringFunctions(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse('abcd'), 'dcba')        

