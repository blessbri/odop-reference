# Version 1 Public Packaging and Reproducibility

The public checkout requires Python 3.9 or later. Its declared runtime
dependency is `jsonschema==4.23.0`; its declared development dependency is
`pytest==8.4.2`.

From a fresh Python 3.9 virtual environment, the following succeeded:

```bash
python -m pip install -e '.[dev]'
python -m pytest
python -m compileall packages
python -m json.tool schemas/odop-json-v1/odop-json-v1.schema.json > /dev/null
python -m json.tool specs/fixtures/v1-json/fixture-manifest.json > /dev/null
```

The Version 1 parser intentionally resolves the approved schema from the
checkout, so the documented installation is editable. No dependency on the
frozen internal repository exists.

