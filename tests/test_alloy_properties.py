import unittest
from materials_science_generator import alloy_properties

class TestAlloyProperties(unittest.TestCase):
    def test_simulate_alloy_name(self):
        name = alloy_properties.simulate_alloy_name()
        self.assertIsInstance(name, str)
        self.assertEqual(len(name), 10)

    def test_simulate_alloy_composition(self):
        composition = alloy_properties.simulate_alloy_composition(num_elements=5)
        self.assertIsInstance(composition, dict)
        self.assertEqual(len(composition), 5)
        for element in composition.values():
            self.assertIsInstance(element, float)
            self.assertGreaterEqual(element, 0)
            self.assertLessEqual(element, 100)

    def test_simulate_element_name(self):
        name = alloy_properties.simulate_element_name()
        self.assertIsInstance(name, str)
        self.assertEqual(len(name), 2)

    def test_simulate_atomic_percentage(self):
        percentage = alloy_properties.simulate_atomic_percentage()
        self.assertIsInstance(percentage, float)
        self.assertGreaterEqual(percentage, 0)
        self.assertLessEqual(percentage, 100)

    def test_simulate_alloy_properties(self):
        properties = alloy_properties.simulate_alloy_properties(num_samples=1)
        self.assertIsInstance(properties, list)
        self.assertEqual(len(properties), 1)
        property_dict = properties[0]
        self.assertIn('name', property_dict)
        self.assertIn('composition', property_dict)
        self.assertIn('density', property_dict)
        self.assertIn('melting_point', property_dict)

if __name__ == '__main__':
    unittest.main()
