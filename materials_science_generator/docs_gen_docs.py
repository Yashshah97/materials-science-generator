"""
Module to generate documentation for the project.

This module uses the built-in `help` function and `sys.modules` dictionary to generate documentation.
"""

import sys
import inspect

def get_module_name():
    """Get the name of this module."""
    return __name__

def get_module_docstring():
    """Get the docstring of this module."""
    return __doc__

def get_function_docs(module):
    """
    Get the docstrings of all functions in a given module.

    Args:
        module (module): The module to extract function docstrings from.

    Returns:
        list: A list of tuples containing the function name and its docstring.
    """
    docs = []
    for name, func in inspect.getmembers(module):
        if inspect.isfunction(func) or inspect.ismethod(func):
            doc = inspect.getdoc(func)
            if doc is not None:
                docs.append((name, doc))
    return docs

def generate_documentation():
    """Generate documentation for the project."""
    module_name = get_module_name()
    module_docstring = get_module_docstring()

    print(f"# {module_name} Documentation")
    print(module_docstring)

    functions = get_function_docs(sys.modules[module_name])
    for name, doc in functions:
        print(f"\n## {name}")
        print(doc)

if __name__ == "__main__":
    generate_documentation()
