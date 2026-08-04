# Open-Source Exclusion Report

The public repository contains only the approved Version 1 subset. The
following categories were excluded from the frozen baseline:

| Excluded category or path | Reason |
| --- | --- |
| `.git/`, `.agents/`, `.venv/`, `.pytest_cache/`, `__pycache__/`, `.DS_Store` | Local metadata, environment, cache, or generated output. |
| `adapters/`, `deploy/`, `sdk/`, `implementation/`, `vision/` | Outside the approved Version 1 public capability. |
| `packages/deployment-ports/`, `packages/external-ports/`, `packages/persistence-ports/`, `packages/protocol-processing/`, `packages/verification/` | Future-scope contracts or adapters not included in Version 1. |
| `test/protocol/test_replay_contracts.py`, `test/protocol/test_verification_contracts.py`, deployment/external/persistence/projection/transport tests | Not Version 1 public parser/validator scope. |
| `docs/PHASE_*`, `docs/RC_*`, internal planning, and non-Version-1 ADRs | Internal process or future-scope material not needed to build, test, govern, or use public Version 1. |
| Root `LICENSE.md` | Not a license grant; replaced by proposed public `LICENSE`. |

No secrets, credentials, local configuration, virtual environments, generated
bytecode, or known private commercial material was copied.

