import unittest
from materials_science_generator import lattice_properties

class TestLatticeProperties(unittest.TestCase):

    def test_simulate_lattice_constant(self):
        self.assertGreaterEqual(lattice_properties.simulate_lattice_constant(), 3.0)
        self.assertLessEqual(lattice_properties.simulate_lattice_constant(), 10.0)

    def test_simulate_atomic_radius(self):
        self.assertGreaterEqual(lattice_properties.simulate_atomic_radius(), 1.5)
        self.assertLessEqual(lattice_properties.simulate_atomic_radius(), 4.0)

    def test_simulate_cohesive_energy(self):
        self.assertGreaterEqual(lattice_properties.simulate_cohesive_energy(), -10.0)
        self.assertLessEqual(lattice_properties.simulate_cohesive_energy(), 10.0)

    def test_simulate_bulk_modulus(self):
        self.assertGreaterEqual(lattice_properties.simulate_bulk_modulus(), 50.0)
        self.assertLessEqual(lattice_properties.simulate_bulk_modulus(), 200.0)

    def test_simulate_poissons_ratio(self):
        self.assertGreaterEqual(lattice_properties.simulate_poissons_ratio(), 0.1)
        self.assertLessEqual(lattice_properties.simulate_poissons_ratio(), 0.5)

if __name__ == '__main__':
    unittest.main()
