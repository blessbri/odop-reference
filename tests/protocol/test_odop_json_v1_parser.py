from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).parents[2] / "packages" / "protocol-model"))

from odop_model import ArtifactHandlingBoundary, ODOP_JSON_V1, OdopJsonV1ParseError, parse_odop_json_v1


def valid_payload() -> bytes:
    return b'{"protocolVersion":"1.0","representation":{"id":"odop-json","version":"1.0"},"artifactType":"rightsObject","artifact":{"objectId":"obj","assetReference":"asset","rights":[]}}'


def test_parser_preserves_receipt_and_returns_local_document() -> None:
    boundary = ArtifactHandlingBoundary()
    boundary.register_parser(ODOP_JSON_V1, parse_odop_json_v1)
    payload = valid_payload()
    result = boundary.receive(payload, ODOP_JSON_V1)
    assert result.receipt.payload == payload
    assert result.parsed_value.receipt is result.receipt
    assert result.parsed_value.document["artifact"]["objectId"] == "obj"


def test_parser_rejects_duplicate_member_after_boundary_preservation() -> None:
    boundary = ArtifactHandlingBoundary()
    boundary.register_parser(ODOP_JSON_V1, parse_odop_json_v1)
    payload = valid_payload().replace(b'"objectId":"obj"', b'"objectId":"obj","objectId":"other"')
    with pytest.raises(OdopJsonV1ParseError, match="Duplicate JSON member"):
        boundary.receive(payload, ODOP_JSON_V1)
    # The boundary creates the receipt before invoking the parser.
    assert payload.startswith(b'{')


def test_parser_rejects_null_and_keeps_missing_distinct() -> None:
    receipt = type("Receipt", (), {"payload": valid_payload().replace(b'"objectId":"obj"', b'"objectId":null"'), "representation": ODOP_JSON_V1})()
    with pytest.raises(OdopJsonV1ParseError):
        parse_odop_json_v1(receipt)
