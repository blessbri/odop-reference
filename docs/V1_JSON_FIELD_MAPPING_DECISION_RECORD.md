# V1 JSON Field Mapping Decision Record

**Status:** Design draft only; no code or machine-readable Schema.

## Envelope

| Member | Type / presence / null | Classification | Source |
|---|---|---|---|
| protocolVersion | string / required / prohibited | Supplied version identifier | 10.1–10.3, 10.9, 24.3, 24.8 |
| representation | object / required / prohibited | Supplied descriptor | 10.2–10.3, 24.2–24.3 |
| artifactType | string rightsObject / required / prohibited | Supplied root classification | 12.1–12.4, 13.1, 24.3 |
| artifact | object / required / prohibited | Supplied Rights Object | 13.1–13.3, 24.3 |

Protocol version value is 1.0. Representation descriptor has id odop-json and
version 1.0. These are delegated representation choices, not registry, media,
or interoperability claims. Object-member order has no semantic meaning.
[10.2–10.3, 24.2–24.3]

## Rights Object and Right fields

| Object | Member | Type / presence | Classification | Source / boundary |
|---|---|---|---|---|
| Rights Object | objectId | string / required | Authoritative identifier | 11.2–11.3, 13.2–13.3; opaque |
| Rights Object | assetReference | string / required | Opaque external reference | 11.7, 12.5, 13.3–13.4 |
| Rights Object | rights | array / required, zero or more | Supplied collection | 12.3–12.4, 13.3, 13.5 |
| Rights Object | metadata | object / optional | Opaque descriptive material | 13.3, 13.7, 13.11 |
| Rights Object | initialHolder | string / optional | Opaque supplied principal reference | 12.7, 13.3, 13.6; no derivation |
| Rights Object | verificationInformation | object / optional | Supplied non-authoritative material | 12.9, 13.8, 19.2 |
| Right | rightId | string / required | Authoritative identifier | 11.2, 11.4, 14.2–14.3 |
| Right | policies | array / required, zero or more | Supplied collection | 14.3, 14.7, 15.1–15.4 |
| Right | events | array / required, zero or more | Supplied collection | 14.3–14.4, 16.1–16.3 |
| Right | lifecycleStatus | string / optional | Non-authoritative supplied derived value | 14.5; no replay/check |
| Right | suppliedHolder | string / optional | Non-authoritative supplied holder | 14.6, 18.1–18.6; no derivation |
| Right | verificationInformation | object / optional | Supplied non-authoritative material | 14.8, 19.2 |

All fields above prohibit null; missing and null remain distinct. Identifiers
retain received spelling and have no local normalization/equality/resolution.
[11.1, 11.7–11.10, 24.4–24.8]

## Policy and Event fields

| Object | Member | Type / presence | Classification | Source / boundary |
|---|---|---|---|---|
| Policy | policyId | string / required | Supplied identifier in Right scope | 15.2–15.3 |
| Policy | policyReference | string / optional | Opaque external reference | 11.9, 15.5–15.7 |
| Policy | policyMaterial | JSON value excluding null / optional | Opaque supplied material | 15.1, 15.5–15.7 |
| Rights Event | eventId | string / required | Supplied event identity | 11.5, 16.2, 16.5 |
| Rights Event | target | object / required | Canonical Right reference | 11.2, 16.2 |
| Rights Event | eventType | string / required | Supplied classification | 16.4; no allowed-value/effect rule |
| Rights Event | predecessorEventId | string / optional | Supplied chain reference | 11.5, 16.3; no validity claim |
| Rights Event | sequence | JSON integer / required | Supplied chain information | 16.3, 16.9; no continuity/order check |
| Rights Event | payload | JSON value excluding null / optional | Opaque supplied material | 16.5, 16.9 |

Policy metadata, verificationInformation, and extensions are optional objects
with the same opaque/supplied boundary in 15.3, 15.6, and 25.2–25.8. Event
verificationInformation and extensions are optional objects under 16.8 and
25.2–25.8. No policy, event, replay, or verification semantics are assigned.

## Shared shapes, preservation, and compatibility

Canonical Right reference has required non-null objectId and rightId strings.
[11.2–11.4, 12.4, 14.2, 16.2] Every mapped object may have optional extensions
object with opaque namespaced keys. Unknown optional values stay scoped,
preserved, uninterpreted, unmerged, and outside standard fields.
[25.2–25.8, 26.7]

Received UTF-8 bytes are retained before parsing; duplicate member names are
rejected only after retention; no Unicode, URI, date, number, case, or
identifier normalization occurs. Array order is retained but is semantic only
where frozen authority provides it; object order is not semantic.
[15.4, 24.3–24.6, 24.8, 25.4–25.5, 29.7]

Deferred: metadata contents, policy reference/material mutual-presence,
extension-key syntax, resource limits, validation/error detail, fixtures, and
media/binding. No PSE is open: initial state (17.3), holder successor (18.4),
policy semantics (15.5–15.7), extension effects (25.1–25.8), and
verification/trust (19.10–21.9) remain excluded.

**Recommendation:** READY TO AUTHOR MACHINE-READABLE JSON SCHEMA

