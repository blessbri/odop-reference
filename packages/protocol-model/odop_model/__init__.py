"""Representation-neutral ODOP model foundation."""

from .artifact_boundary import ArtifactHandlingBoundary, ArtifactReceipt, RepresentationDescriptor
from .core import CanonicalRightReference, RightRecord, RightsObjectRecord
from .odop_json_v1 import ODOP_JSON_V1, OdopJsonV1ParseError, ParsedOdopJsonV1, parse_odop_json_v1
from .validation import LocalValidationIssue, LocalValidationResult, ResourceLimits, validate_odop_json_v1

__all__ = [
    "ArtifactHandlingBoundary",
    "ArtifactReceipt",
    "RepresentationDescriptor",
    "CanonicalRightReference",
    "RightRecord",
    "RightsObjectRecord",
    "ODOP_JSON_V1",
    "OdopJsonV1ParseError",
    "ParsedOdopJsonV1",
    "parse_odop_json_v1",
    "LocalValidationIssue",
    "LocalValidationResult",
    "ResourceLimits",
    "validate_odop_json_v1",
]
