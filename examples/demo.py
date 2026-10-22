"""Demo for Materials Science Synthetic Data Generator."""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

import materials_science_generator

print("Materials Science Synthetic Data Generator", "v" + materials_science_generator.__version__)
print("modules:", [m for m in dir(materials_science_generator) if not m.startswith('_')])
