"""Print local V1 structural findings for a received JSON file."""

from pathlib import Path
import sys

from odop_model import ArtifactReceipt, ODOP_JSON_V1, validate_odop_json_v1


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python examples/validate_v1.py PATH", file=sys.stderr)
        return 2
    payload = Path(sys.argv[1]).read_bytes()
    result = validate_odop_json_v1(ArtifactReceipt(payload, ODOP_JSON_V1, {}))
    for issue in result.issues:
        print(f"{issue.issue_code} {issue.json_path}: {issue.message}")
    return 1 if result.issues else 0


if __name__ == "__main__":
    raise SystemExit(main())

