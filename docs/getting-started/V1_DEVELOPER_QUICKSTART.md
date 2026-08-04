# Version 1 Developer Quick-Start

1. Create a Python 3.9+ virtual environment.
2. Install development dependencies: `.venv/bin/python -m pip install -e ".[dev]"`.
3. Run `.venv/bin/python -m pytest -q`.
4. Register `ODOP_JSON_V1` with `ArtifactHandlingBoundary` and
   `parse_odop_json_v1`.
5. Use `validate_odop_json_v1` for local structural evidence only.

Do not treat parsed data or LocalValidationResult as replay, verification,
conformance, or interoperability output.
