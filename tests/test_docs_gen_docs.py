"""Smoke tests for docs_gen_docs."""
import unittest

from materials_science_generator import docs_gen_docs


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(docs_gen_docs, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(docs_gen_docs) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
