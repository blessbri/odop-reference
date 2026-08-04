# Version 1 API Overview

Public model exports: `ArtifactHandlingBoundary`, `ArtifactReceipt`,
`RepresentationDescriptor`, `ODOP_JSON_V1`, `parse_odop_json_v1`,
`ParsedOdopJsonV1`, `ResourceLimits`, `validate_odop_json_v1`,
`LocalValidationIssue`, and `LocalValidationResult`.

`parse_odop_json_v1` parses only the approved descriptor. `validate_odop_json_v1`
returns local structural/operational/unsupported issues and retains the receipt.
These APIs provide no replay, verification, registry, transport, persistence,
or conformance behavior.
