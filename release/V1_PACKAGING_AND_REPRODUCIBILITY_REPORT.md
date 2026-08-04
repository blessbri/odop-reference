# Version 1 Packaging and Reproducibility Report

Python requirement is >=3.9. The development dependency set declares pytest
8.4.2 and jsonschema 4.23.0 in pyproject.toml. The documented clean setup is
in PYTHON_TEST_ENVIRONMENT.md: create a virtual environment and install the
project development extras. Package exports, schema path resolution, and fixture
manifest paths were exercised by the passing tests and audit commands.

No undeclared runtime dependency was identified.
