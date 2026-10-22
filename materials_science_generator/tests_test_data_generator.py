'''Module for testing the data generator'''

import unittest
from io import StringIO
import sys

def capture_stdout(func):
    '''Capture stdout'''
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    try:
        func()
    finally:
        sys.stdout = old_stdout
    return new_stdout.getvalue()

class TestDataGenerator(unittest.TestCase):

    def test_generate_data(self):
        data = capture_stdout(lambda: generate_data())
        self.assertGreater(len(data), 0)

if __name__ == '__main__':
    unittest.main()
