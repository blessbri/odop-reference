# ODOP Reference Implementation

ODOP, the Open Digital Ownership Protocol, provides a protocol foundation for
representing digital ownership rights. This repository is the official
reference implementation of Version 1 of the ODOP Reference Implementation.
It is deliberately a bounded local structural toolkit, not a certification or
hosted service.

## Version 1 capability

Version 1 accepts the approved `odop-json` 1.0 representation for a Rights
Object, preserves the received bytes, parses strict UTF-8 JSON, rejects
duplicate member names, evaluates the bundled Draft 2020-12 JSON Schema, and
reports deterministic local structural findings.

```text
ArtifactHandlingBoundary
  → ArtifactReceipt
  → odop-json v1 parser
  → Draft 2020-12 JSON Schema
  → Structural Validator
  → LocalValidationResult
```

Schema validity and `LocalValidationResult` are local structural observations.
They are not claims of protocol validity, protocol conformance,
interoperability, replay, verification, or trust.

Version 1 does **not** implement replay, lifecycle or holder derivation, policy
evaluation, verification, Verification Profiles, registries,
interoperability, conformance, canonicalization, signing, transport,
persistence, recovery, replication, consensus, blockchain, or post-quantum
capabilities.

## Install

Use Python 3.9 or later in a fresh virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
```

The editable install is intentional for Version 1: the frozen parser resolves
the approved schema from this repository checkout.

## Quick start

```bash
python examples/validate_v1.py examples/minimal-rights-object.json
python -m pytest
```

See [the developer quick-start](docs/getting-started/V1_DEVELOPER_QUICKSTART.md)
and [the public API overview](docs/reference/V1_API_OVERVIEW.md).

## Repository layout

- [`protocol/`](protocol/) — frozen ODOP Protocol Specification.
- [`architecture/`](architecture/) — frozen Reference Implementation Architecture.
- [`specs/`](specs/) and [`schemas/`](schemas/) — Version 1 supporting materials.
- [`packages/protocol-model/`](packages/protocol-model/) — public Python model,
  parser, artifact boundary, and structural validator.
- [`tests/`](tests/) — focused Version 1 tests.
- [`docs/`](docs/) and [`release/`](release/) — developer, governance, and
  release records.

## Status and roadmap boundary

Version 1 is frozen and feature-complete. Future work must preserve the frozen
Protocol Specification as the sole semantic authority and follow the published
governance process. This repository does not begin Version 2.

## Contributing, security, and license

Read [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md),
[SECURITY.md](SECURITY.md), [SUPPORT.md](SUPPORT.md), and the
[Code of Conduct](CODE_OF_CONDUCT.md). The proposed public license is Apache
License 2.0; see [LICENSE](LICENSE) and [release/LICENSE_REVIEW.md](release/LICENSE_REVIEW.md).

