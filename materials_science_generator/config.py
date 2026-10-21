"""
Module to store configurable constants and default values.

This module contains configurable constants and their default values used by the materials science synthetic data generator.
"""

class Config:
    """
    Class containing configurable constants and their default values.
    """

    # Lattice properties
    DEFAULT_LATTICE_CONSTANTS = {
        'a': 4.0,  # Angstroms
        'b': 4.0,  # Angstroms
        'c': 10.0,  # Angstroms
        'alpha': 90.0,  # Degrees
        'beta': 90.0,  # Degrees
        'gamma': 120.0  # Degrees
    }

    # Alloy properties
    DEFAULT_ALLOY_PROPERTIES = {
        'composition': 0.5,  # Mole fraction
        'temperature': 298.15,  # Kelvin
        'pressure': 101325  # Pascals
    }

    # Crystal structure types
    CRYSTAL_STRUCTURE_TYPES = ['cubic', 'tetragonal', 'orthorhombic', 'monoclinic', 'triclinic']

    # Alloy type options
    ALLOY_TYPE_OPTIONS = ['binary', 'ternary', 'quaternary']

def get_config():
    """
    Returns the Config class instance.

    :return: Config class instance
    """
    return Config()

# Example usage:
config = get_config()
print(config.DEFAULT_LATTICE_CONSTANTS['a'])
