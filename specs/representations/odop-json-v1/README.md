# Candidate ODOP JSON Interchange Representation Specification Version 1

**Status:** DRAFT — REVIEW REQUIRED  
**Publication status:** Candidate supporting publication only; not approved,
published, frozen, registered, or implementation-authoritative.

## Authority and selected scope

This candidate defines owner-selected representation details delegated by
Protocol 24.3. It does not amend core ODOP meaning; a representation cannot
change standard fields, canonical Right references, event-chain relationships,
profile bindings, or extension meaning. [Protocol 10.2; 24.2; Architecture
Chapters 1–6 and 10]

Rights Object is the only supported root artifact type. Nested Rights, policy
attachments, Rights Events, optional verification information, and extensions
may be mapped only to the extent frozen authority supports them; their detailed
mapping remains deferred. [Protocol 12.1–12.10; 13.1–13.11; 14.1–14.10;
15.1–15.7; 16.1–16.9; 24.3]

## Envelope

A Version 1 document is one top-level JSON object with members
protocolVersion, representation, artifactType, and artifact.

| Member | Role | Class and authority |
|---|---|---|
| protocolVersion | Applicable Protocol version | Delegated placement implementing Protocol 10.1, 10.3, 10.9, 24.3, 24.8 |
| representation | Representation descriptor | Delegated choice under 10.2–10.3, 24.2–24.3 |
| artifactType | Root artifact kind | Delegated choice under 12.1–12.4, 13.1, 24.3 |
| artifact | Root artifact representation | Delegated choice under 12.1–12.3, 13.1–13.3, 24.3 |

The representation descriptor is an object with id `odop-json` and
version `1.0`. These identify this representation only; they are not a
Protocol version, registry entry, media type, or interoperability claim.
[Protocol 10.2–10.3, 10.9; 24.2–24.3, 24.10]

## References and extensions

Object, Right, asset, principal, policy, event, and other references are opaque
JSON strings unless frozen authority expressly requires another form. This is a
delegated encoding choice; it creates no syntax, namespace, normalization,
equality, resolution, global-uniqueness, or legal-identity rule. [Protocol
11.1–11.10; 13.2; 14.2; 15.2; 16.2; 24.3]

A canonical Right reference is an object containing objectId and rightId. It
implements the frozen pair without assigning either component new meaning.
[Protocol 11.2–11.4; 12.4; 14.2; 16.2; 24.3]

Optional extension material is under an extensions object using opaque namespaced
keys. This is a placement choice only; keys are not globally allocated and this
document supplies no namespace syntax, allocation process, or extension
definition. [Protocol 24.3; 25.3, 25.10; 26.7] Unknown optional extension
values must remain scoped and must not be interpreted, relabeled, merged,
dropped, or promoted into standard fields. [Protocol 25.2, 25.4–25.8]

## JSON handling and preservation

| Rule | Class | Authority and consequence |
|---|---|---|
| Retain complete received UTF-8 bytes before parsing. | Delegated encoding plus inherited preservation. | 24.3; 24.4; 25.4–25.5. Parsed/reserialized JSON is never presumed byte-equivalent. |
| UTF-8 only; top-level object only. | Delegated representation choices. | 24.3, 24.10. |
| Reject duplicate names after retaining bytes. | Delegated well-formedness choice. | 24.3–24.4, 25.5, 29.7; no byte loss/rewrite. |
| No implicit Unicode, identifier, URI, date, number, or case normalization. | Delegated fidelity choice. | 11.1, 11.7–11.10; 24.4–24.6, 24.8; 25.5. |
| Missing and null are distinct; null is prohibited absent future field authorization. | Delegated choice. | 24.3, 24.8. |
| Object-member order has no semantic meaning. | Delegated choice. | 24.2–24.3. |
| Array order is retained; semantic meaning arises only from frozen authority. | Delegated fidelity choice. | 15.4; 24.2–24.4; 25.5. |
| Resource limits are required before parser authorization; values remain unset. | Deferred security rule. | 29.7; Architecture Chapter 19. |

## Schema, media, and exclusions

A future matching schema uses JSON Schema Draft 2020-12. This is an
owner-selected schema-language choice delegated by 24.3 and left open by 24.10.
No machine-readable schema or constraint is created here.

No registered media type is defined. A .odop.json suffix may be non-normative
local guidance only; it is not a media type, binding, registry entry, or
Protocol requirement. [Protocol 24.3, 24.9–24.10]

This candidate defines no parser, serializer, structural validator, replay,
holder derivation, verification, trust, profile, registry, transport,
interoperability, conformance, canonicalization, signing, conversion, durable
record, consensus, recovery, replication, or post-quantum behavior. [Protocol
17–21, 24.5–24.10, 26–28, 31]

## Deferred decisions and PSE screen

Before schema/parser work: exact Protocol version value; Rights Object field
mapping/names/types/cardinality/null rules/metadata; nested Right, policy,
event, verification-information, and extension mappings; payload encoding;
mandatory fields; error/resource-limit details; structural validation rules,
fixtures, and any media/binding material.

No PSE is proposed, required, or open. Initial state (17.3), holder-successor
representation (18.4), policy semantics (15.5–15.7), extension effects
(25.1–25.8), and verification/trust (19.10–21.9) are excluded or unmapped. A
later mapping that needs one must stop and escalate under Architecture Chapter
27 and Protocol Chapter 34.

**Recommendation:** READY TO COMPLETE REPRESENTATION FIELD MAPPING

## Approved field-mapping annex

The complete owner-selected Rights Object, Right, Policy, Rights Event, shared
reference, preservation, compatibility, and PSE field matrix is incorporated in
[V1 JSON Field Mapping Decision Record](../../../docs/V1_JSON_FIELD_MAPPING_DECISION_RECORD.md).
It is part of this draft candidate only and does not create a Schema, parser,
or validation behavior.
