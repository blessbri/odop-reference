# Public API Surface

The public Python package is `odop_model`.

| API | Purpose |
| --- | --- |
| `ArtifactHandlingBoundary` | Preserves received bytes and dispatches only explicitly registered parsers. |
| `ArtifactReceipt` | Local immutable receipt containing payload, representation, and intake context. |
| `RepresentationDescriptor` | Local representation identifier tuple. |
| `ODOP_JSON_V1` | Descriptor for `odop-json` version `1.0`. |
| `parse_odop_json_v1` | Local strict UTF-8 JSON parsing and optional Schema checking. |
| `ParsedOdopJsonV1` | Local parsed document retaining its original receipt. |
| `validate_odop_json_v1` | Local structural issue aggregation. |
| `LocalValidationIssue`, `LocalValidationResult` | Local structural evidence types. |
| `ResourceLimits` | Optional local limit configuration points. |
| `CanonicalRightReference`, `RightRecord`, `RightsObjectRecord` | Opaque local model relationships. |

Unsupported: replay, lifecycle and holder derivation, policy evaluation,
verification/trust, registries, interoperability, conformance,
canonicalization, signing, transport, persistence, recovery, replication,
consensus, blockchain, and post-quantum capabilities.

