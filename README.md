# ODOP Reference Implementation

<p align="center">
  <strong>Open Digital Ownership Protocol (ODOP)</strong><br>
  <em>A reference implementation for representing digital ownership without binding to a blockchain, database, cloud provider, transport protocol, or cryptographic implementation.</em>
</p>

<p align="center">
  <strong>Technology-neutral. Vendor-neutral. Future-ready.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-v1.0.0--rc.1-blue" alt="Version v1.0.0-rc.1">
  <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/license-Apache%202.0-green" alt="Apache License 2.0">
  <img src="https://img.shields.io/badge/status-Frozen%20Baseline-success" alt="Frozen Baseline">
</p>

---

## Why ODOP?

Most digital ownership systems are tightly coupled to one technology stack.

ODOP separates **protocol semantics** from **implementation technology**,
enabling independent implementations while preserving a common protocol
foundation.

## Version 1 Architecture

```text
ArtifactHandlingBoundary
        │
        ▼
ArtifactReceipt
        │
        ▼
ODOP JSON Parser
        │
        ▼
Draft 2020-12 JSON Schema
        │
        ▼
Structural Validator
        │
        ▼
LocalValidationResult
```

---

## Feature Matrix

| Capability | Version 1 |
| --- | --- |
| JSON Representation | ✅ |
| JSON Schema | ✅ |
| Parser | ✅ |
| Structural Validation | ✅ |
| Deterministic Issue Model | ✅ |
| Fixture Catalogue | ✅ |
| Integration Tests | ✅ |
| Replay | ❌ |
| Verification | ❌ |
| Registry | ❌ |
| Interoperability | ❌ |
| Conformance | ❌ |

---

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest
```

Validate:

```bash
python examples/validate_v1.py examples/minimal-rights-object.json
```

---

## Repository Layout

```text
protocol/
architecture/
packages/
schemas/
specs/
tests/
examples/
docs/
release/
```

---

## FAQ

### Why not blockchain?

Version 1 intentionally focuses on protocol representation and local structural
processing. Blockchain integration is outside Version 1 scope.

### Why technology-neutral?

The protocol is designed so implementations are not tied to one runtime,
storage engine, cloud provider, or cryptographic stack.

### Is this production-ready?

Version 1 is a **reference implementation** and bounded local structural
toolkit. It is not a protocol certification, interoperability suite, or
production trust infrastructure.

---

## Roadmap

### ✅ Version 1

- Representation
- Schema
- Parser
- Structural Validator
- Fixtures
- Integration Tests

### 🔜 Version 2

- Replay

### 🔜 Version 3

- Verification

### 🔮 Future

- Enterprise SDK
- Cloud Services
- Post-Quantum Evolution

---

## Community

Contributions are welcome.

Please read:

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [GOVERNANCE.md](GOVERNANCE.md)
- [SECURITY.md](SECURITY.md)
- [SUPPORT.md](SUPPORT.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

---

## License

Apache License 2.0

See [LICENSE](LICENSE) and [NOTICE](NOTICE).

---

## Vision

Build an open ecosystem for digital ownership that is:

- Open
- Technology-neutral
- Vendor-neutral
- Extensible
- Long-term maintainable

---

**© Blessbridge Global Trading LLC**
