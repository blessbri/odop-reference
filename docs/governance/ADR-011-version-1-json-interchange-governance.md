# ADR-011: Version 1 JSON Interchange Governance Baseline

**Status:** Proposed for V1-P0 review  
**Scope:** Governance and planning only; no supporting publication or implementation
is approved by this ADR.

## Context

The owner selected a Version 1 product direction limited to one bounded
JSON-based interchange representation, one versioned JSON Schema,
received-representation preservation, parsing, and structural validation.
Protocol 24.3 requires a supported representation to be separately published
and versioned; Protocol 24.10 does not select JSON, schema syntax, media type,
or transport binding. The Architecture requires preservation before
interpretation and keeps implementation architecture subordinate to protocol
authority (Chapters 1–6 and 10).

## Decision

V1-P0 establishes only the governance baseline for a future candidate JSON
representation and schema. Its authority boundary is:

- the frozen Protocol Specification supplies all protocol semantics;
- a future versioned JSON representation/schema may supply only
  representation-level detail delegated by Protocol 24.3 and maintained under
  34.5; and
- implementation may consume only independently reviewed/published supporting
  material through the Architecture’s artifact boundary and ports.

V1-P0 does not select JSON field names, document/object shapes, identifier
encoding, extension layout, schema rules, media type, transport binding,
validation checks, or fixture outcomes.

## Required records and review gates

The V1-P0 records are the capability-scope statement, publication-governance
record, exact Protocol/Architecture source matrix, PSE screening record,
traceability entry, limitation, and deferred-work record.

A proposed normative supporting-publication statement must cite its exact frozen
Protocol source. Any proposed statement that needs lifecycle, holder, policy,
trust, verification-result, extension, or other core semantic meaning outside
that source is stopped and recorded as a potential PSE under Architecture
Chapter 27 and Protocol Chapter 34.

## Consequences

- No candidate representation specification or JSON Schema is created.
- No parser, serializer, preservation, validation, replay, verification,
  registry, interoperability, conformance, recovery, replication, consensus,
  blockchain, or post-quantum behavior is added.
- A future implementation phase cannot begin until the required supporting
  publications have independently passed review and publication gates.
- Version 1 remains limited to its explicit scope; excluded capabilities cannot
  be inferred from architecture, tests, local configuration, or deployment.

