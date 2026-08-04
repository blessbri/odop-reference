# V1 JSON Parser Architecture

The parser is a registered adapter at the common Artifact Handling Boundary.
The boundary creates an ArtifactReceipt before parser invocation; the parser
decodes only descriptor 1.0 / odop-json / 1.0, rejects duplicate JSON members,
validates the approved Draft 2020-12 Schema, and returns ParsedOdopJsonV1 as a
local representation retaining that receipt.

Authority: Protocol 24.3–24.4, 24.8, 25.4–25.8, 29.7; Architecture Chapters
10, 13, 16, and 19. It performs no replay, lifecycle/holder derivation,
verification, policy evaluation, registry access, normalization,
canonicalization, signing, interoperability, or conformance work.

# V1 JSON Parser Test Plan

Tests cover: exact receipt payload preservation; successful parsing of the
approved descriptor/envelope; duplicate-member rejection after receipt creation;
and schema rejection of prohibited null. Future tests require separately
authorized resource limits, fixtures, and validation-result conventions.

No PSE is open: parser behavior is limited to approved representation/schema
rules. Any later parser rule requiring core semantic interpretation stops under
Architecture Chapter 27 and Protocol Chapter 34.
