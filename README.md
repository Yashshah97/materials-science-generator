# Materials Science Synthetic Data Generator

This project generates realistic synthetic data for materials science applications, allowing researchers to test and train models without relying on sensitive or proprietary real-world data. Built with pure Python, the code is easy to understand, modify, and integrate into existing workflows. With a focus on crystal lattice and alloy properties, this tool helps accelerate research in fields like materials engineering and computational chemistry.

## What makes it unique

Combines crystal lattice and alloy properties with a statistically-plausible fake data generator for testing — a niche where few ready-made tools exist.

## Features

- **`materials_science_generator/config.py`** — Module to store configurable constants and default values
- **`materials_science_generator/data_generator.py`** — Main module for generating synthetic data
- **`materials_science_generator/lattice_properties.py`** — Module containing functions for simulating crystal lattice properties
- **`materials_science_generator/alloy_properties.py`** — Module containing functions for simulating alloy properties
- **`materials_science_generator/tests_test_data_generator.py`** — Test module for the data generator
- **`materials_science_generator/docs_gen_docs.py`** — Module to generate documentation for the project

## Tech stack

- **Python 3** — pure standard library, **zero external dependencies**
- **unittest** for the test suite (6/6 module suites passing)
- Local-first: no network calls, no API keys, runs anywhere Python runs

## How to run

```bash
git clone https://github.com/Yashshah97/materials-science-generator.git
cd materials-science-generator

# run the demo
python3 examples/demo.py

# run the tests
python3 -m unittest discover -s tests -t .
```

No installation step is needed — there is nothing to `pip install`.

## Project structure

```
materials-science-generator/
├── materials_science_generator/
│   ├── config.py
│   ├── data_generator.py
│   ├── lattice_properties.py
│   ├── alloy_properties.py
│   ├── tests_test_data_generator.py
│   ├── docs_gen_docs.py
├── tests/               # unittest suite (verified passing)
├── examples/demo.py     # runnable demo (verified)
├── docs/
└── README.md
```

See [docs/PLAN.md](docs/PLAN.md) for the architecture and
[docs/usage.md](docs/usage.md) for API notes.

## About

Domain: **materials-science** · Archetype: **generator** ·
Built autonomously by JARVIS on 2026-10-21. MIT licensed.
