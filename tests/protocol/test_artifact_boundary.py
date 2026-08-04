from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[2] / "packages" / "protocol-model"))

from odop_model import ArtifactHandlingBoundary, RepresentationDescriptor


def descriptor() -> RepresentationDescriptor:
    return RepresentationDescriptor("1.0", "example-published-representation", "1.0")


def test_unsupported_representation_preserves_exact_received_bytes() -> None:
    boundary = ArtifactHandlingBoundary()
    payload = b'  {"extension": [1, 2]}  '
    result = boundary.receive(payload, descriptor(), {"transport": "test"})
    assert not result.supported
    assert result.receipt.payload == payload
    assert result.receipt.intake_context == {"transport": "test"}
    assert result.parsed_value is None
    assert result.limitation is not None


def test_registered_handler_receives_the_preserved_receipt() -> None:
    boundary = ArtifactHandlingBoundary()
    seen: list[bytes] = []

    def parser(receipt):
        seen.append(receipt.payload)
        return {"local": "parsed"}

    boundary.register_parser(descriptor(), parser)
    result = boundary.receive(b"input", descriptor())
    assert result.supported
    assert result.parsed_value == {"local": "parsed"}
    assert seen == [b"input"]
