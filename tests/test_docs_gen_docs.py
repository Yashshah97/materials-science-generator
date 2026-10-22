import unittest
from materials_science_generator import docs_gen_docs

class TestDocsGenDocs(unittest.TestCase):

    def test_get_module_name(self):
        self.assertEqual(docs_gen_docs.get_module_name(), __name__)

    def test_get_module_docstring(self):
        self.assertIsNotNone(docs_gen_docs.get_module_docstring())

    def test_get_function_docs(self):
        functions = docs_gen_docs.get_function_docs(__import__(__name__))
        self.assertGreater(len(functions), 0)

if __name__ == "__main__":
    unittest.main()
