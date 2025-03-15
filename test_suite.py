import unittest

# Import your test modules
from tests import test_module1
from tests.example import test_functions
from tests.example.string import test_string_functions

# Aggregate all tests into a test suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_module1))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_functions))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(test_string_functions))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
