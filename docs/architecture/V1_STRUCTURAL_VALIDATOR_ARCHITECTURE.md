# V1 Structural Validator Architecture and Tests

The validator calls the approved parser with schema evaluation deferred, then
aggregates parser failures and all Draft 2020-12 schema errors into sorted local
issues. Ordering is JSON Pointer, issue code, then message. Results retain the
original ArtifactReceipt and are local structural/operational/unsupported
evidence, never protocol conformance.

ResourceLimits exposes maximum received bytes, nesting depth, object members,
array length, string length, and reported issues. Every value defaults to unset;
no deployment numeric policy is selected. The current implementation enforces
only configured received-byte and reported-issue bounds; remaining categories
are configuration points pending separately authorized enforcement.

Tests cover deterministic schema issues with JSON Pointer paths, receipt
preservation, and configured byte-limit reporting. Authority: Protocol
22.3–22.4, 23.1–23.10, 24.3–24.8, 25.4–25.7, 29.7; Architecture Chapters
10–12, 19, 23, and 27. No PSE is open.
