# Version 1 Test and Verification Report

Environment: Python 3.9.6; pytest 8.4.2.

| Command | Result |
|---|---|
| .venv/bin/python -m pytest -q | 23 passed in 0.08s |
| .venv/bin/python -m compileall -q packages adapters test | passed |
| .venv/bin/python -m json.tool schemas/odop-json-v1/odop-json-v1.schema.json | passed |
| .venv/bin/python -m json.tool specs/fixtures/v1-json/fixture-manifest.json | passed |
| .venv/bin/python -m pytest -q test/protocol/test_odop_json_v1_parser.py test/protocol/test_v1_structural_validation.py test/protocol/test_v1_json_integration.py | 7 passed in 0.05s |

These are local implementation tests, not Protocol conformance or
interoperability evidence.
