"""Local parser for the approved draft ODOP JSON representation v1.

This module performs no replay, verification, normalization, or interpretation.
"""

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator

from .artifact_boundary import ArtifactReceipt, RepresentationDescriptor


ODOP_JSON_V1 = RepresentationDescriptor("1.0", "odop-json", "1.0")


class OdopJsonV1ParseError(ValueError):
    """Local representation parse or structural-schema failure."""


def _reject_duplicate_members(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise OdopJsonV1ParseError(f"Duplicate JSON member name: {key}")
        result[key] = value
    return result


def _schema() -> Mapping[str, Any]:
    root = Path(__file__).resolve().parents[3]
    schema_path = root / "schemas" / "odop-json-v1" / "odop-json-v1.schema.json"
    with schema_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


_VALIDATOR = Draft202012Validator(_schema())


@dataclass(frozen=True)
class ParsedOdopJsonV1:
    """Local parsed representation; it never replaces the receipt payload."""

    receipt: ArtifactReceipt
    document: Mapping[str, Any]


def parse_odop_json_v1(receipt: ArtifactReceipt, *, validate_schema: bool = True) -> ParsedOdopJsonV1:
    """Decode one approved JSON representation after receipt preservation."""

    if receipt.representation != ODOP_JSON_V1:
        raise OdopJsonV1ParseError("Receipt does not identify ODOP JSON representation 1.0.")
    try:
        text = receipt.payload.decode("utf-8", errors="strict")
        document = json.loads(text, object_pairs_hook=_reject_duplicate_members)
    except UnicodeDecodeError as error:
        raise OdopJsonV1ParseError("Received representation is not valid UTF-8.") from error
    except json.JSONDecodeError as error:
        raise OdopJsonV1ParseError("Received representation is not valid JSON.") from error
    if not isinstance(document, dict):
        raise OdopJsonV1ParseError("ODOP JSON representation requires a top-level object.")
    errors = sorted(_VALIDATOR.iter_errors(document), key=lambda error: (list(error.path), error.validator))
    if validate_schema and errors:
        raise OdopJsonV1ParseError(f"JSON Schema validation failed: {errors[0].message}")
    return ParsedOdopJsonV1(receipt=receipt, document=document)
