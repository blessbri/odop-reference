# V1 Structural Validation and Error Model Specification

**Status:** Design draft only. It authorizes no validator, fixture, runtime
change, or protocol-conformance claim.

## 1. Boundary and authority

Structural handling is limited to the approved JSON representation and Schema.
It is distinct from verification, admission, and operational failure. [Protocol
22.3–22.4, 23.1–23.10, 24.3–24.8; Architecture Chapters 10–12 and 23]

Schema validity is a local representation-structural result, not protocol
validity, conformance, replay, lifecycle, holder, policy, verification, trust,
or interoperability. [Protocol 23.8, 27.1–27.9, 28.1–28.10]

| Condition | Classification | Stop rule / preservation |
|---|---|---|
| Receipt/preservation failure | Local operational | Stop intake; report separately. |
| UTF-8 failure | Structural fatal | Stop decoding; receipt bytes remain retained. |
| JSON syntax failure | Structural fatal | Stop parsing; receipt bytes remain retained. |
| Duplicate member | Structural fatal | Stop parsing after receipt preservation. |
| Descriptor mismatch | Unsupported | Do not interpret; retain receipt and report limitation. |
| Schema structural failure | Structural | Do not perform semantic processing. |
| Resource-limit failure | Local operational | Stop affected operation; retain received bytes where acquired. |
| Unsupported optional capability | Unsupported | Preserve/report; do not assign meaning. |
| Protocol-semantic validation | Out of scope | Stop and route a needed new rule to PSE screening. |

Sources: Protocol 10.6, 22.3–22.4, 23.3–23.8, 24.4, 24.8, 25.4–25.7,
29.7; Architecture Chapters 10, 19, 23, and 27.

## 2. Local validation-result model

A future local result record has: issueCode, issueCategory, severity, jsonPath
when available, message, representationId, representationVersion, issueClass,
sourceRule, and receiptProvenance.

IssueClass is exactly structural, localOperational, unsupported, or semantic.
Semantic is a containment category only and never resolves protocol meaning.
Severity is fatal, error, or notice. This is local implementation evidence, not
a Protocol validation report or conformance result. [Protocol 19.4–19.6,
23.3, 23.7–23.8; Architecture Chapters 12 and 23]

## 3. Initial local issue-code catalogue

| Code | Category / severity | Class | Source rule |
|---|---|---|---|
| V1-REP-001 | Unsupported representation descriptor / error | unsupported | 10.6; 24.8 |
| V1-ENC-001 | Invalid UTF-8 / fatal | structural | 24.3–24.4 |
| V1-JSON-001 | Invalid JSON syntax / fatal | structural | 24.3; 29.7 |
| V1-JSON-002 | Duplicate member name / fatal | structural | 24.3–24.4, 25.5, 29.7 |
| V1-JSON-003 | Non-object root / fatal | structural | Approved representation envelope; 24.3 |
| V1-SCHEMA-001 | Schema constraint failure / error | structural | 23.2–23.3; 24.3 |
| V1-SCHEMA-002 | Prohibited null / error | structural | Approved mapping; 24.3, 24.8 |
| V1-SCHEMA-003 | Unknown standard member / error | structural | Approved Schema/mapping; 24.3 |
| V1-SCHEMA-004 | Missing required member / error | structural | Approved Schema/mapping; 23.2, 24.3 |
| V1-SCHEMA-005 | Incorrect JSON type / error | structural | Approved Schema/mapping; 23.2, 24.3 |
| V1-RES-001 | Resource limit exceeded / fatal | localOperational | 29.7; Architecture 19 |

Codes are local identifiers. They are not Protocol registry error codes, and
they do not extend the Protocol’s pending error-code registry. [Protocol 23.9–23.10, 26.1–26.9]

## 4. Deterministic reporting rules

Receipt, UTF-8, JSON syntax, duplicate-member, non-object-root, descriptor, and
resource-limit fatal failures stop the affected parsing stage after preservation.
Schema evaluation runs only after successful decoding/parsing/descriptor checks.

Future Schema errors are ordered by JSON Pointer path lexicographically, then
by Schema keyword, then by stable local code. JSON paths use JSON Pointer
notation; the root is the empty pointer. This is local report representation,
not Protocol field-location syntax. [Protocol 23.7, 23.10; 24.3]

Messages use stable code-led templates and cite the violated representation or
Schema rule; they do not include stack traces, provider details, or arbitrary
payload values. Received bytes remain the ArtifactReceipt payload after every
failure. [Protocol 24.4; 25.4–25.5; 29.7; Architecture 10 and 19]

## 5. Resource-limit decision record

Future parser/validator configuration requires named limits for maximum received
bytes, nesting depth, object-member count, array length, string length, and
reported-issue count. No numeric value is selected. Values need owner-approved
security/deployment configuration and tests before runtime authorization.
[Protocol 29.7, 29.12; Architecture Chapters 19, 22, and 25]

## 6. Responsibility matrix

| Check | Owner |
|---|---|
| Receipt creation and byte preservation | Artifact Handling Boundary |
| UTF-8, JSON syntax, duplicate names, top-level object, descriptor | Parser |
| Approved shape/type/required/null/unknown-member constraints | JSON Schema validator |
| Error ordering, local result records, resource limits, cross-field structural checks approved later | Future structural validator |
| Identifier equality, event-chain continuity, lifecycle, holder, policy, semantic extension meaning | Future protocol-semantic validation/replay |
| Profile, signature, trust, evidence, verification result | Future verification capability |

## 7. Fixture and negative-test plan

Future fixtures/tests cover: valid minimum Rights Object; valid nested Rights,
Policy, and Event forms; invalid UTF-8; malformed JSON; duplicate members;
wrong descriptor/version; missing members; prohibited null; wrong types; unknown
standard members; preserved unknown extensions; and each named resource-limit
category.

Each fixture must identify representation/schema version, source rule, expected
local code/class, receipt-preservation expectation, and no semantic outcome.
Replay/profile/interoperability/conformance fixtures are excluded. [Protocol
23.2–23.8, 24.3–24.8, 25.4–25.7, 27.5–27.9]

## 8. PSE screen and recommendation

No PSE is proposed, required, or open. Initial state (17.3), holder successor
(18.4), policy semantics (15.5–15.7), event-type effects (16.4), extension
effects (25.1–25.8), and verification/trust (19.10–21.9) are excluded.

**Recommendation:** READY TO IMPLEMENT STRUCTURAL VALIDATION AND FIXTURES

