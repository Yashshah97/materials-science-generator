"""
Module containing functions for simulating crystal lattice properties.

This module generates statistically-plausible fake data for testing purposes,
specifically for crystal lattice and alloy properties.
"""

import random
import math

def simulate_lattice_constant():
    """
    Simulate the lattice constant (a) of a material in Angstroms (Å).

    Returns:
        float: A random value between 3.0 Å and 10.0 Å.
    """
    return round(random.uniform(3.0, 10.0), 2)

def simulate_atomic_radius():
    """
    Simulate the atomic radius of a material in Angstroms (Å).

    Returns:
        float: A random value between 1.5 Å and 4.0 Å.
    """
    return round(random.uniform(1.5, 4.0), 2)

def simulate_cohesive_energy():
    """
    Simulate the cohesive energy of a material in eV/atom.

    Returns:
        float: A random value between -10.0 eV/atom and 10.0 eV/atom.
    """
    return round(random.uniform(-10.0, 10.0), 2)

def simulate_bulk_modulus():
    """
    Simulate the bulk modulus of a material in GPa.

    Returns:
        float: A random value between 50.0 GPa and 200.0 GPa.
    """
    return round(random.uniform(50.0, 200.0), 2)

def simulate_poissons_ratio():
    """
    Simulate the Poisson's ratio of a material.

    Returns:
        float: A random value between 0.1 and 0.5.
    """
    return round(random.uniform(0.1, 0.5), 2)
