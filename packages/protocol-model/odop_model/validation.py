"""Local V1 structural validation evidence; never a protocol conformance result."""

from dataclasses import dataclass
from typing import Optional, Tuple

from .artifact_boundary import ArtifactReceipt
from .odop_json_v1 import ODOP_JSON_V1, OdopJsonV1ParseError, _VALIDATOR, parse_odop_json_v1


@dataclass(frozen=True)
class ResourceLimits:
    max_received_bytes: Optional[int] = None
    max_nesting_depth: Optional[int] = None
    max_object_members: Optional[int] = None
    max_array_length: Optional[int] = None
    max_string_length: Optional[int] = None
    max_reported_issues: Optional[int] = None


@dataclass(frozen=True)
class LocalValidationIssue:
    issue_code: str
    issue_category: str
    severity: str
    json_path: str
    message: str
    representation_id: str
    representation_version: str
    issue_class: str
    source_rule: str


@dataclass(frozen=True)
class LocalValidationResult:
    receipt: ArtifactReceipt
    issues: Tuple[LocalValidationIssue, ...]


def _pointer(path: object) -> str:
    parts = [str(part).replace("~", "~0").replace("/", "~1") for part in path]
    return "" if not parts else "/" + "/".join(parts)


def _issue(code: str, category: str, severity: str, path: str, message: str, issue_class: str, source: str) -> LocalValidationIssue:
    return LocalValidationIssue(code, category, severity, path, message, "odop-json", "1.0", issue_class, source)


def validate_odop_json_v1(receipt: ArtifactReceipt, limits: ResourceLimits = ResourceLimits()) -> LocalValidationResult:
    """Aggregate local parse/schema/limit issues while retaining the receipt."""
    if receipt.representation != ODOP_JSON_V1:
        return LocalValidationResult(receipt, (_issue("V1-REP-001", "unsupported representation descriptor", "error", "", "Unsupported representation descriptor.", "unsupported", "Protocol 10.6, 24.8"),))
    if limits.max_received_bytes is not None and len(receipt.payload) > limits.max_received_bytes:
        return LocalValidationResult(receipt, (_issue("V1-RES-001", "resource limit exceeded", "fatal", "", "Received byte limit exceeded.", "localOperational", "Protocol 29.7"),))
    try:
        parsed = parse_odop_json_v1(receipt, validate_schema=False)
    except OdopJsonV1ParseError as error:
        message = str(error)
        code = "V1-JSON-001"
        if message.startswith("Received representation is not valid UTF-8"):
            code = "V1-ENC-001"
        elif message.startswith("Duplicate JSON member"):
            code = "V1-JSON-002"
        elif message.startswith("ODOP JSON representation requires"):
            code = "V1-JSON-003"
        return LocalValidationResult(receipt, (_issue(code, "JSON structural failure", "fatal", "", message, "structural", "Protocol 24.3-24.4, 29.7"),))
    issues = []
    for error in _VALIDATOR.iter_errors(parsed.document):
        code = "V1-SCHEMA-001"
        if error.instance is None: code = "V1-SCHEMA-002"
        elif error.validator == "required": code = "V1-SCHEMA-004"
        elif error.validator == "type": code = "V1-SCHEMA-005"
        elif error.validator == "additionalProperties": code = "V1-SCHEMA-003"
        elif error.validator == "not": code = "V1-SCHEMA-002"
        issues.append(_issue(code, "schema constraint failure", "error", _pointer(error.path), error.message, "structural", "Protocol 23.2-23.3, 24.3"))
    issues.sort(key=lambda issue: (issue.json_path, issue.issue_code, issue.message))
    if limits.max_reported_issues is not None:
        issues = issues[:limits.max_reported_issues]
    return LocalValidationResult(receipt, tuple(issues))
