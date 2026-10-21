import unittest
from materials_science_generator import data_generator

class TestDataGenerator(unittest.TestCase):
    def test_generate_random_string(self):
        self.assertIsInstance(data_generator.generate_random_string(10), str)
        self.assertEqual(len(data_generator.generate_random_string(10)), 10)

    def test_generate_synthetic_data(self):
        data = data_generator.generate_synthetic_data()
        self.assertIsInstance(data, dict)
        self.assertIn('lattice_constant', data)
        self.assertIn('bulk_modulus', data)
        self.assertIn('shear_modulus', data)
        self.assertIn('poisson_ratio', data)
        self.assertIn('alloy_name', data)
        self.assertIn('crystal_structure', data)

if __name__ == '__main__':
    unittest.main()
