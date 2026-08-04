# V1 Fixture Catalogue and Integration Test Package

The machine-readable catalogue is `specs/fixtures/v1-json/fixture-manifest.json`.
Each entry declares its ID, class, representation, frozen/approved source,
expected local issue code or no issue, receipt preservation, and the explicit
non-semantic disclaimer. Integration tests cover the approved boundary → receipt
→ parser → Schema → validator flow, exact-byte preservation, opaque extension
retention, deterministic issue ordering, configured limits, and absence of
normalization or semantic interpretation.

Fixtures do not claim replay, lifecycle, holder, policy, verification, trust,
interoperability, or conformance behavior. Resource values are isolated test
configuration only. No PSE is open; excluded semantic paths remain excluded.
