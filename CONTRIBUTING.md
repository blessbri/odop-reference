# Contributing

Thank you for improving the ODOP reference implementation. By contributing,
you confirm that you have the right to submit the contribution under the
repository license once the maintainer accepts it.

## Contribution boundary

The frozen Protocol Specification is the only authority for ODOP protocol
semantics. A contribution must not add, reinterpret, or silently resolve
protocol meaning. Supporting-publication changes and implementation changes
are reviewed separately; see [GOVERNANCE.md](GOVERNANCE.md).

Before opening a pull request:

```bash
python -m pip install -e '.[dev]'
python -m pytest
python -m compileall packages
```

Keep Version 1 scope bounded. Do not add replay, verification, registry,
interoperability, conformance, transport, persistence, or other future-scope
features without an approved, separately scoped decision.

