# Candidate ODOP JSON Schema Package Version 1

**Status:** DRAFT — REVIEW REQUIRED  
**Contents:** odop-json-v1.schema.json is a Draft 2020-12 schema for the
approved candidate representation mapping. It is not published, frozen, or
implementation-authoritative.

## Traceability

Every constraint carries an x-odop-source annotation. The source is either the
approved V1 JSON Field Mapping Decision Record plus its exact frozen Protocol
citation, or an inherited Protocol representation requirement.

Key mappings: envelope/version (10.1–10.3, 24.3, 24.8); Rights Object
(12–13); Right (14); Policy (15); Rights Event (16); canonical Right reference
(11.2–11.4); preservation/extensions (24.4–24.6, 25.2–25.8).

## Unresolved decisions

The schema intentionally leaves metadata contents, policyReference/policyMaterial
mutual presence, extension-key syntax, resource limits, validation issue codes,
fixtures, media type, and bindings unresolved. Duplicate-member detection is a
parser concern and cannot be expressed by JSON Schema. No lifecycle, replay,
holder derivation, verification, trust, registry, interoperability, conformance,
canonicalization, signing, transport, or conversion behavior is defined.

## PSE screening

No PSE is proposed, required, or open. The schema does not constrain initial
state, holder-successor representation, policy semantics, extension effects, or
verification/trust semantics. If a future constraint needs one, it must stop and
escalate under Architecture Chapter 27 and Protocol Chapter 34.

