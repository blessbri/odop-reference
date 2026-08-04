# ODOP Reference Implementation Architecture

**Version:** 1.0  
**Status:** Architecture-frozen publication edition  
**Related protocol:** ODOP Protocol Specification Version 1.0  
**Normative status:** Non-normative

## Document Status and Intended Use

This is a non-normative recommended implementation architecture for ODOP. The ODOP Protocol Specification is the sole authority for protocol semantics, conformance, and maintenance. This publication does not amend, replace, narrow, extend, or reinterpret that specification.

## Abstract

The reference architecture is modular and protocol-centered. It separates the protocol kernel from concrete integrations, preserves received and retained material, treats views as rebuildable, and supports independent verification without making infrastructure evidence protocol authority.

## How to Read This Document

Protocol terms retain their specified meanings. Architecture recommendations, diagrams, deployment profiles, package layouts, and templates are explanatory. Potential semantic changes are recorded under Chapter 27 and routed to Protocol Specification Chapter 34.

## Table of Contents

1. Purpose, Scope, and Authority Boundary
2. Relationship to the Frozen ODOP Protocol Specification
3. Non-Normative Conventions and Terminology
4. Architectural Goals and Design Principles
5. Reference Scope and Explicit Non-Goals
6. Protocol Traceability and Semantic Guardrails
7. Reference Deployment Overview
8. Logical Architecture Overview
9. Component Responsibilities and Dependency Rules
10. Protocol Artifact-Handling Boundary
11. Rights Processing and Replay Architecture
12. Verification Architecture
13. Persistence, Event Store, and Evidence Retention
14. Projections, Queries, and Rebuildable Read Models
15. External Integration Ports
16. Transport and Interoperability Adapters
17. Reference Durable-Record and Ledger Profile
18. Cryptographic Provider and Key-Management Integration
19. Security Architecture
20. Privacy and Data-Handling Architecture
21. Reliability, Recovery, and Preservation Architecture
22. Observability and Operational Administration
23. Testing, Conformance Support, and Interoperability Validation
24. Reference Component Packaging and Dependency Boundaries
25. Deployment Topologies and Configuration Profiles
26. Architecture Decision Records and Local Configuration Governance
27. Protocol-Semantic Escalation and Implementation-Issue Handling
28. Known Limitations and Deferred Implementation Work
29. Maintenance of This Architecture Document

Appendix A. Protocol-to-Architecture Traceability Matrix  
Appendix B. Logical Component and Trust-Boundary Diagrams  
Appendix C. Reference Data Classification  
Appendix D. Reference Processing Sequences  
Appendix E. Adapter Interface Catalogue  
Appendix F. Reference Deployment Profiles  
Appendix G. Test Strategy and Fixture Catalogue  
Appendix H. Architecture Decision Record Template  
Appendix I. Protocol-Semantic Escalation Record Template  
Appendix J. Glossary and Acronyms  
Appendix K. Illustrative Reference Repository Layout

## Revision History

| Version | Date | Status | Summary |
|---|---|---|---|
| 1.0 | 2026-08-03 | Architecture-frozen | Initial approved publication edition. |

## 1. Purpose, Scope, and Authority Boundary

This architecture covers recommended component boundaries, preservation, verification, integrations, operations, testing, and governance for ODOP 1.0. It does not define protocol behavior, require a technology stack, or determine legal, identity, policy, payment, custody, or product outcomes.

## 2. Relationship to the Frozen ODOP Protocol Specification

The architecture uses the frozen ODOP 1.0 baseline. It follows published profiles, representations, registries, fixtures, errata, and revisions only according to their published authority. Architecture updates follow protocol maintenance; they never anticipate or substitute for it.

## 3. Non-Normative Conventions and Terminology

This document uses ordinary-language recommendations. Protocol terms retain their specified meaning. Architecture-local terms include protocol kernel, port, adapter, deployment profile, received representation, derived view, and protocol-semantic escalation. Illustrations are not protocol definitions.

## 4. Architectural Goals and Design Principles

The architecture promotes semantic fidelity, clear boundaries, independent assessment, preservation, portability, interoperability support, security, privacy, observability, testability, and maintainability. It separates facts, evidence, local decisions, and views; isolates infrastructure; preserves before transforming; makes uncertainty visible; and escalates semantic concerns.

## 5. Reference Scope and Explicit Non-Goals

In scope are protocol-aware handling, verification, persistence, projections, integrations, deployment, security, privacy, operations, testing, and governance. Out of scope are semantic definitions, legal or identity authority, policy language, payments, custody, mandatory technologies, and product models.

## 6. Protocol Traceability and Semantic Guardrails

The traceability matrix maps authoritative sources to components, tests, evidence, supported scope, and limitations. It cites rather than recreates protocol rules. Guardrails prevent local admission, infrastructure evidence, adapter behavior, or views from becoming protocol authority; ambiguity triggers Chapter 27.

## 7. Reference Deployment Overview

The illustrative deployment receives and preserves artifacts, invokes protocol processing and available verification, retains evidence, serves rebuildable views, and uses external services through ports. Logical areas are transport, artifact handling, kernel, verification, retention, projections, operations, and external integrations.

## 8. Logical Architecture Overview

The logical core consists of the protocol kernel, verification, workflow, preservation and evidence, and projection and query capabilities. Transport routes through artifact handling; external systems use ports; operations manages local services. No component independently defines ODOP semantics.

## 9. Component Responsibilities and Dependency Rules

Adapters own technology translation; the artifact boundary owns coordination; the kernel applies published behavior; verification reports assessment; persistence retains material; projections derive views; operations administers. Dependencies point inward: kernel code does not import concrete infrastructure.

## 10. Protocol Artifact-Handling Boundary

The boundary coordinates receipt, preservation, capability identification, representation-aware parsing, routing, and export. It keeps received representations distinct from parsed and derived forms, and transport metadata distinct from protocol artifacts. It does not infer missing facts or semantic effects.

## 11. Rights Processing and Replay Architecture

The coordinator retrieves retained material and invokes the protocol kernel. Replay produces rebuildable derived results and may produce an implementation-level trace of inputs, scope, and limitations. Local workflow, concurrency, persistence, and notification controls do not alter protocol results.

## 12. Verification Architecture

Verification is independently callable. It distinguishes supplied material, retained material, independently acquired evidence, and local observations. Profile resolution, provider access, evidence retrieval, and report generation are separable. Reports are implementation observations, not protocol artifacts or product decisions.

## 13. Persistence, Event Store, and Evidence Retention

Retention covers received representations, historical material, verification material, published support material, durable-record evidence, and selected operational evidence. The event-store port provides abstract append and retrieval; the durable-record port provides infrastructure evidence. Views and caches are derived and rebuildable.

## 14. Projections, Queries, and Rebuildable Read Models

Projections, indexes, snapshots, search, reports, and analytics are derived from retained sources and applicable kernel support. They record input scope, freshness, provenance, and limitations, and can be rebuilt. Query responses distinguish retained artifacts, derived views, observations, and product data.

## 15. External Integration Ports

Ports isolate cryptographic, trust-material, identity, policy, time, asset, storage, durable-record, transport, notification, and publication-retrieval capabilities. Contracts expose bounded capability, provenance, side effects, and limitations. External decisions remain external.

## 16. Transport and Interoperability Adapters

Adapters support local import, export, query, interoperability, notification, and administration bindings. They separate transport envelopes and delivery outcomes from artifacts and protocol-facing results, and route supported paths through the common artifact boundary.

## 17. Reference Durable-Record and Ledger Profile

The illustrative deployment may use a permissioned, replicated durable-record system for persistence, replication, inclusion, ordering, provenance, or finality evidence. It does not introduce tokens, balances, accounts, or smart-contract execution. Its order and finality are not ODOP replay semantics.

## 18. Cryptographic Provider and Key-Management Integration

Abstract ports isolate reviewed cryptographic providers, key management, certificates, trusted time, secure channels, and evidence retention. Published profiles govern protocol-relevant behavior. Unsupported capability is reported, not silently replaced with a local algorithm or trust interpretation.

## 19. Security Architecture

Security protects inputs, retained material, external dependencies, cryptographic operations, administration, projections, and supply chains. Threat modeling, least privilege, protected retention, safe parsing, audit, and incident response are local controls, not protocol authority.

## 20. Privacy and Data-Handling Architecture

The architecture supports minimization, controlled disclosure, privacy-aware queries and observability, restricted external retrieval, and documented retention. Privacy controls may restrict local access or retention but do not rewrite artifacts or change protocol results.

## 21. Reliability, Recovery, and Preservation Architecture

The preservation set may include artifacts, received forms, support material, verification and durable-record evidence, configuration context, and operations records. Backup, restoration, migration, and replay-based rebuild preserve provenance and report unavailable historical capability without inventing facts.

## 22. Observability and Operational Administration

Data, control, and observation planes are separate. Metrics, logs, traces, audit records, health, configuration, and recovery actions are implementation evidence. Configuration is reviewed, versioned, tested, and auditable, and does not create a semantic override.

## 23. Testing, Conformance Support, and Interoperability Validation

Layered testing covers kernel support, artifacts, verification, persistence, views, adapters, operations, security, privacy, recovery, and interoperability. Fixtures are identified as published or local. Tests demonstrate bounded implementation evidence, not universal conformance or semantic authority.

## 24. Reference Component Packaging and Dependency Boundaries

Stable categories cover model and processing, verification, persistence, projections, external ports, adapters, workflow, operations, and tests. Public interfaces are capability-oriented; provider details remain internal. Package names and repository layouts may evolve without becoming ODOP requirements.

## 25. Deployment Topologies and Configuration Profiles

Illustrative topologies include development, integration, replicated reference, verifier, archive, and hybrid deployments. Versioned configuration profiles identify topology, adapters, supported material, retention, security, privacy, operations, and limits. They are not ODOP profiles or conformance levels.

## 26. Architecture Decision Records and Local Configuration Governance

ADRs record material component, technology, configuration, operations, migration, and exception decisions. Every ADR includes a protocol-semantic assessment and links to Chapter 27 when needed. Configuration records preserve scope, approval, rollback, and historical context without changing semantics.

## 27. Protocol-Semantic Escalation and Implementation-Issue Handling

Any apparent need to change artifact meaning, processing, validation, replay, verification, extensions, registries, representations, conformance, or interoperability is contained, evidenced, tracked, and routed to Protocol Specification Chapter 34. No local code, test, configuration, adapter, or architecture statement resolves ODOP semantics.

## 28. Known Limitations and Deferred Implementation Work

The implementation records unsupported or partial capability, provider and deployment constraints, operational limits, security and privacy limitations, and deferred work. A limitation remains local unless resolving it requires a semantic interpretation, in which case it is escalated under Chapter 27.

## 29. Maintenance of This Architecture Document

This architecture is maintained independently of the Protocol Specification. Editorial, architectural, illustrative, implementation-alignment, and published-protocol-alignment updates are reviewed and versioned. A potential semantic change is never an architecture update; it is a Chapter 27 escalation.

## Appendix A. Protocol-to-Architecture Traceability Matrix

The baseline matrix maps Protocol Specification Chapters 1–34 and Appendices A–H to architecture chapters, components, and evidence. Detailed entries cite the exact source, implementation location, tests, fixtures, supported scope, and limitations. Status values are Planned, Implemented, Tested, Limited, Unsupported, Under Review, Escalated, and Superseded; none is a conformance determination.

## Appendix B. Logical Component and Trust-Boundary Diagrams

Logical diagrams depict inward dependencies from adapters through ports to the kernel and verification capabilities. Trust-boundary diagrams distinguish external clients and providers, the deployment edge, the controlled core, and privileged administration. Additional views distinguish retained material, evidence, derived outputs, and operational planes.

## Appendix C. Reference Data Classification

Reference classes include received and retained protocol material, published support material, supplied and acquired verification material, observations, durable-record evidence, derived views, operational evidence, product data, and secrets. Local handling labels are illustrative and do not determine ODOP meaning.

## Appendix D. Reference Processing Sequences

Illustrative sequences cover inbound handling; processing, retention, and durable record; verification; projection rebuild; external resolution; and recovery. Equivalent implementations may reorder non-semantic local steps if responsibility boundaries and protocol-facing behavior remain unchanged.

## Appendix E. Adapter Interface Catalogue

The catalogue covers representation, repository, history, event-store, durable-record, cryptographic, trust, time, registry, identity, policy, asset, transport, notification, configuration, and observability ports. Every contract records bounded capability, provenance, errors, side effects, and limitations.

## Appendix F. Reference Deployment Profiles

Illustrative profiles are DEV-1 (local development), INT-1 (integration), REF-1 (replicated reference), VER-1 (independent verification), and ARC-1 (preservation archive). They describe local deployment choices and are not protocol profiles, certification classes, or conformance levels.

## Appendix G. Test Strategy and Fixture Catalogue

The catalogue defines test layers, fixture categories, catalogue metadata, expected-result discipline, execution records, interoperability exercises, lifecycle, data protection, and release evidence. Published ODOP fixtures are always distinguished from local fixtures.

## Appendix H. Architecture Decision Record Template

The ADR template records context, decision, alternatives, affected boundaries, traceability, consequences, verification, exception controls, and lifecycle. It requires an explicit protocol-semantic assessment and escalation reference when a semantic concern is possible.

## Appendix I. Protocol-Semantic Escalation Record Template

The template records the non-resolution statement, sources, context, evidence, competing outcomes, impact, containment, maintenance path, published disposition, follow-up, and closure. It explicitly cannot resolve ODOP semantics.

## Appendix J. Glossary and Acronyms

Architecture-local terminology includes adapter, ADR, artifact-handling boundary, deployment profile, durable-record evidence, implementation evidence, port, projection, protocol kernel, received representation, replay trace, supported scope, and verification observation. Protocol terminology remains defined solely by the Protocol Specification.

## Appendix K. Illustrative Reference Repository Layout

An illustrative layout uses `packages/` for core categories, `adapters/` for concrete integrations, `deploy/` for profile assets, `specs/` for support material and fixtures, `test/` for layered testing, and `docs/` for ADRs, traceability, limitations, escalations, and runbooks. It is version-specific and non-normative.
