# Version 1 Capability Scope and Exclusions

**Status:** V1-P0 planning record — not an approved, published, frozen, or
implementation-authoritative supporting publication.

## Proposed capability boundary

Subject to future supporting-publication review, Version 1 is limited to one
versioned JSON interchange representation, one corresponding versioned JSON
Schema, exact received-representation preservation, parsing, and structural
validation.

The boundary follows Protocol 24.2–24.4, which permits an independently
versioned representation and requires preservation where needed, and Architecture
Chapters 10 and 16, which separate receipt/preservation from parsing and
transport.

## Explicit exclusions

| Exclusion | Exact frozen authority |
|---|---|
| Replay, lifecycle derivation, and replay outcomes | Protocol 17.1–17.9; Architecture Chapter 11 |
| Holder-change processing | Protocol 18.3–18.5; Architecture Chapter 11 |
| Verification, trust, cryptographic processing, and Verification Profiles | Protocol 19.1–19.10, 20.1–20.8, 21.1–21.9; Architecture Chapters 12 and 18 |
| Registry operation or entries | Protocol 26.1–26.9, 33.1–33.10; Architecture Chapter 15 |
| Interoperability and conformance claims | Protocol 27.1–27.9, 28.1–28.10; Architecture Chapter 23 |
| Cross-format conversion | Protocol 24.5–24.6, 25.5 |
| Durable records, recovery, replication, consensus, and blockchain | Protocol 22.7–22.11, 31.1–31.10; Architecture Chapters 13, 17, and 21 |
| Post-quantum implementation | Protocol 20.5, 21.6, 29.5; Architecture Chapter 18 |

## Non-authority rule

A future JSON representation/schema can define only the representation details
required by Protocol 24.3. It must not alter core standard-field, canonical
Right-reference, event-chain, Verification-Envelope profile-binding, or
extension meaning (24.2). It must not use a JSON default to change missing,
unknown, or unsupported feature meaning (24.8).

No capability claim is made by this record.

