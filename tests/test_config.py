import unittest
from materials_science_generator import config

class TestConfig(unittest.TestCase):

    def test_get_config(self):
        config_instance = config.get_config()
        self.assertIsInstance(config_instance, config.Config)

    def test_config_class_attributes(self):
        config_instance = config.get_config()
        self.assertEqual(config_instance.DEFAULT_LATTICE_CONSTANTS['a'], 4.0)
        self.assertEqual(config_instance.DEFAULT_ALLOY_PROPERTIES['composition'], 0.5)
        self.assertEqual(config_instance.CRYSTAL_STRUCTURE_TYPES, ['cubic', 'tetragonal', 'orthorhombic', 'monoclinic', 'triclinic'])
        self.assertEqual(config_instance.ALLOY_TYPE_OPTIONS, ['binary', 'ternary', 'quaternary'])

    def test_get_config_returns_same_instance(self):
        config_instance1 = config.get_config()
        config_instance2 = config.get_config()
        self.assertIs(config_instance1, config_instance2)

if __name__ == '__main__':
    unittest.main()
