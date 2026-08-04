from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parents[2] / "packages" / "protocol-model"))
from odop_model import ArtifactReceipt, ODOP_JSON_V1, ResourceLimits, validate_odop_json_v1


def receipt(payload: bytes) -> ArtifactReceipt:
    return ArtifactReceipt(payload, ODOP_JSON_V1, {})


def test_schema_issues_are_deterministic_and_preserve_receipt() -> None:
    payload = b'{"protocolVersion":"1.0","representation":{"id":"odop-json","version":"1.0"},"artifactType":"rightsObject","artifact":{"objectId":null,"assetReference":3,"rights":[]}}'
    result = validate_odop_json_v1(receipt(payload))
    assert result.receipt.payload == payload
    assert [issue.issue_code for issue in result.issues] == ["V1-SCHEMA-005", "V1-SCHEMA-002"]
    assert [issue.json_path for issue in result.issues] == ["/artifact/assetReference", "/artifact/objectId"]


def test_resource_limit_has_no_default_and_is_configurable() -> None:
    result = validate_odop_json_v1(receipt(b"{}"), ResourceLimits(max_received_bytes=1))
    assert result.issues[0].issue_code == "V1-RES-001"
