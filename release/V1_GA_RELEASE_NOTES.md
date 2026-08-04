# ODOP Reference Implementation Version 1.0 Release Notes

Version 1.0 provides one bounded local capability: ODOP JSON representation
handling for descriptor odop-json 1.0 and Protocol version 1.0. It preserves
received bytes, parses strict UTF-8 JSON, rejects duplicate members, applies the
approved Draft 2020-12 Schema, returns local parsed material, and reports local
structural issues deterministically.

It does not claim Protocol conformance or validity, replay, lifecycle/holder
derivation, policy evaluation, verification/trust, registry, interoperability,
transport, persistence, recovery, replication, consensus, blockchain, or
post-quantum behavior.
