"""Representation-neutral core relationships from Protocol Specification Chapters 11 and 12.

Identifiers and asset references are opaque values here. Their syntax,
normalization, equality, and resolution are not defined by this package.
"""

from dataclasses import dataclass
from typing import Iterable, Tuple


@dataclass(frozen=True)
class CanonicalRightReference:
    """The protocol's pair of owning object identifier and Right identifier."""

    object_id: object
    right_id: object


@dataclass(frozen=True)
class RightRecord:
    """A Right identified within its owning Rights Object."""

    right_id: object


@dataclass(frozen=True)
class RightsObjectRecord:
    """Aggregate context with opaque asset reference and independently addressed Rights."""

    object_id: object
    asset_reference: object
    rights: Tuple[RightRecord, ...]

    @classmethod
    def from_rights(
        cls,
        object_id: object,
        asset_reference: object,
        rights: Iterable[RightRecord],
    ) -> "RightsObjectRecord":
        return cls(object_id, asset_reference, tuple(rights))

    def canonical_references(self) -> Tuple[CanonicalRightReference, ...]:
        return tuple(CanonicalRightReference(self.object_id, right.right_id) for right in self.rights)
