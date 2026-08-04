from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[2] / "packages" / "protocol-model"))
from odop_model import ArtifactHandlingBoundary, ArtifactReceipt, ODOP_JSON_V1, ResourceLimits, parse_odop_json_v1, validate_odop_json_v1


def payload(artifact: str) -> bytes:
    return ('{"protocolVersion":"1.0","representation":{"id":"odop-json","version":"1.0"},"artifactType":"rightsObject","artifact":' + artifact + '}').encode()


def test_full_flow_preserves_unknown_extension_without_interpretation() -> None:
    raw = payload('{"objectId":"O%CC%88","assetReference":"A","rights":[{"rightId":"R","policies":[{"policyId":"P","policyMaterial":{"x":1}}],"events":[{"eventId":"E","target":{"objectId":"O%CC%88","rightId":"R"},"eventType":"future","sequence":1,"payload":{"x":true}}]}],"extensions":{"example:unknown":{"z":1}},"verificationInformation":{"opaque":true}}')
    boundary = ArtifactHandlingBoundary(); boundary.register_parser(ODOP_JSON_V1, parse_odop_json_v1)
    parsed = boundary.receive(raw, ODOP_JSON_V1).parsed_value
    result = validate_odop_json_v1(parsed.receipt)
    assert parsed.receipt.payload == raw and result.receipt.payload == raw
    assert result.issues == ()
    assert parsed.document["artifact"]["extensions"]["example:unknown"] == {"z": 1}
    assert parsed.document["artifact"]["objectId"] == "O%CC%88"


def test_integration_reports_deterministic_pointer_and_limit() -> None:
    raw = payload('{"objectId":null,"assetReference":3,"rights":[],"unknown":true}')
    result = validate_odop_json_v1(ArtifactReceipt(raw, ODOP_JSON_V1, {}))
    assert [i.json_path for i in result.issues] == sorted(i.json_path for i in result.issues)
    assert result.receipt.payload == raw
    limited = validate_odop_json_v1(ArtifactReceipt(raw, ODOP_JSON_V1, {}), ResourceLimits(max_received_bytes=1))
    assert limited.issues[0].issue_code == "V1-RES-001"
