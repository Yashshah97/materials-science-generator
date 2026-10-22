"""
Module containing functions for simulating alloy properties.

This module generates statistically-plausible fake data for testing purposes.
"""

import random
import string

def simulate_alloy_name(length=10):
    """
    Generate a random alloy name.

    Args:
        length (int): Length of the generated name. Defaults to 10.

    Returns:
        str: Random alloy name.
    """
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def simulate_alloy_composition(num_elements=5):
    """
    Generate a random alloy composition.

    Args:
        num_elements (int): Number of elements in the alloy. Defaults to 5.

    Returns:
        dict: Random alloy composition as a dictionary.
    """
    return {simulate_element_name(): simulate_atomic_percentage() for _ in range(num_elements)}

def simulate_element_name():
    """
    Generate a random element name.

    Returns:
        str: Random element name.
    """
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(2))

def simulate_atomic_percentage():
    """
    Generate a random atomic percentage.

    Returns:
        float: Random atomic percentage between 0 and 100.
    """
    return round(random.uniform(0, 100), 2)

def simulate_alloy_properties(num_samples=10):
    """
    Generate a list of statistically-plausible fake alloy properties.

    Args:
        num_samples (int): Number of samples to generate. Defaults to 10.

    Returns:
        list: List of dictionaries containing alloy properties.
    """
    return [
        {
            'name': simulate_alloy_name(),
            'composition': simulate_alloy_composition(),
            'density': round(random.uniform(5, 20), 2),
            'melting_point': round(random.uniform(500, 2000), 2)
        } for _ in range(num_samples)
    ]
