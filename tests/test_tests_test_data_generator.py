import unittest
from materials_science_generator import tests_test_data_generator

class TestTestDataGenerator(unittest.TestCase):

    def test_capture_stdout(self):
        captured = tests_test_data_generator.capture_stdout(lambda: 'Hello, World!')
        self.assertEqual(captured.strip(), 'Hello, World!')

    def test_TestDataGenerator_instance(self):
        TestDataGenerator = tests_test_data_generator.TestDataGenerator
        self.assertTrue(isinstance(TestDataGenerator(), TestDataGenerator))

if __name__ == '__main__':
    unittest.main()
