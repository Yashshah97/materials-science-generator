"""
Materials Science Synthetic Data Generator.

This module contains the main function for generating synthetic data for crystal lattice and alloy properties.
"""

import random
import string

def generate_random_string(length):
    """Generate a random string of given length."""
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def generate_synthetic_data():
    """
    Generate synthetic data for crystal lattice and alloy properties.

    Returns:
        dict: A dictionary containing the generated data.
    """
    data = {
        'lattice_constant': round(random.uniform(3.5, 4.2), 2),
        'bulk_modulus': round(random.uniform(150, 250), 2),
        'shear_modulus': round(random.uniform(50, 100), 2),
        'poisson_ratio': round(random.uniform(0.25, 0.35), 2),
        'alloy_name': generate_random_string(10),
        'crystal_structure': random.choice(['FCC', 'BCC', 'HCP']),
    }
    return data

def main():
    """
    Main function to generate synthetic data.

    Usage:
        python -m materials_science_generator.data_generator
    """
    print(generate_synthetic_data())

if __name__ == '__main__':
    main()
