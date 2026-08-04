# Version 1 Public Test and Verification Report

Public-release verification was run in a fresh Python 3.9.6 virtual
environment with pytest 8.4.2 and jsonschema 4.23.0.

| Check | Command | Result |
| --- | --- | --- |
| Full focused suite | `python -m pytest` | 11 passed |
| Parser, validator, and integration subset | `python -m pytest tests/protocol/test_odop_json_v1_parser.py tests/protocol/test_v1_structural_validation.py tests/protocol/test_v1_json_integration.py` | 7 passed |
| Compilation | `python -m compileall packages` | passed |
| Schema JSON syntax | `python -m json.tool schemas/odop-json-v1/odop-json-v1.schema.json` | passed |
| Fixture-manifest JSON syntax | `python -m json.tool specs/fixtures/v1-json/fixture-manifest.json` | passed |
| Public import | `python -c 'import odop_model'` | passed |
| Example | `python examples/validate_v1.py examples/minimal-rights-object.json` | passed (no findings) |

These tests establish only the bounded local Version 1 behavior. They do not
assert protocol conformance, interoperability, replay, verification, or trust.

