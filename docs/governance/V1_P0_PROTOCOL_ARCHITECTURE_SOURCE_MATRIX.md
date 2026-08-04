# V1-P0 Exact Protocol and Architecture Source Matrix

**Status:** Planning matrix only. Protocol citations are the sole authority for
any future normative supporting-publication statement.

| Planned statement or boundary | Exact Protocol authority | Architecture support | V1-P0 disposition |
|---|---|---|---|
| A JSON representation is separate from core ODOP semantics and protocol version. | 10.2–10.4; 24.1–24.3 | Chapters 1–3, 10, 16 | Planned; no representation created |
| A supported representation must be published/versioned and state identity, mapping, data/field rules, reference encoding, extensions, profile relation, and defined media/binding details. | 24.3 | Chapters 10, 16, 24 | Planned; all details undecided |
| Received representation is preserved when needed; parsed/local forms are not byte-equivalent replacements. | 24.4; 25.4–25.5 | Chapters 10, 13, 21 | Planned V1 preservation boundary |
| JSON defaults must not change missing/unknown/unsupported feature meaning. | 10.6; 24.8; 25.6–25.7 | Chapters 6, 10, 27 | Stop rule |
| JSON/media/schema/transport choices are not supplied by core ODOP. | 24.10 | Chapters 16, 25 | Owner-selected JSON direction only; all concrete choices deferred |
| Structural validation is distinct from verification and operational failure. | 22.3–22.4; 23.1–23.10 | Chapters 10–12, 23 | Planned, bounded; rules not selected |
| Unknown optional extensions are preserved without local semantics. | 25.2–25.7 | Chapters 10, 13, 16 | Planned; layout and schema rules deferred |
| Cross-format conversion is not allowed without published disposition. | 24.5–24.6; 25.5 | Chapters 10, 16 | Excluded |
| Replay/lifecycle and holder outcomes need separate core support. | 17.3–17.9; 18.3–18.5 | Chapter 11 | Excluded; PSE if future scope needs unresolved meaning |
| Verification profiles, canonicalization, algorithms, and trust procedure are separate profile material. | 19.10; 20.2–20.8; 21.1–21.9 | Chapters 12, 18 | Excluded |
| Registry categories create no entries and governance is pending. | 26.2, 26.8–26.9; 33.10 | Chapters 15, 17, 18 | Excluded |
| Fixtures/conformance/interoperability need separately published material and scoped evidence. | 27.4–27.9; 28.2–28.10 | Chapter 23; Appendix G | Excluded |
| Supporting material is versioned/preserved and cannot change core semantics. | 10.1–10.5; 34.1–34.9 | Chapters 6, 26–29 | V1 publication governance rule |

No matrix row authorizes implementation or resolves a protocol gap.

