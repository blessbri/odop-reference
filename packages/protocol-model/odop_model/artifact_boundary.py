"""Architecture Chapter 10 representation-neutral artifact boundary."""

from dataclasses import dataclass
from typing import Callable, Mapping, Optional


@dataclass(frozen=True)
class RepresentationDescriptor:
    protocol_version: str
    representation_id: str
    representation_version: str


@dataclass(frozen=True)
class ArtifactReceipt:
    payload: bytes
    representation: RepresentationDescriptor
    intake_context: Mapping[str, str]


@dataclass(frozen=True)
class ArtifactIntakeResult:
    receipt: ArtifactReceipt
    supported: bool
    parsed_value: Optional[object]
    limitation: Optional[str]


Parser = Callable[[ArtifactReceipt], object]


class ArtifactHandlingBoundary:
    """Preserves received bytes before invoking an explicit parser."""

    def __init__(self) -> None:
        self._parsers: dict[RepresentationDescriptor, Parser] = {}

    def register_parser(self, descriptor: RepresentationDescriptor, parser: Parser) -> None:
        self._parsers[descriptor] = parser

    def receive(
        self,
        payload: bytes,
        representation: RepresentationDescriptor,
        intake_context: Optional[Mapping[str, str]] = None,
    ) -> ArtifactIntakeResult:
        receipt = ArtifactReceipt(payload, representation, dict(intake_context or {}))
        parser = self._parsers.get(representation)
        if parser is None:
            return ArtifactIntakeResult(
                receipt,
                False,
                None,
                "Unsupported representation; received bytes preserved without interpretation.",
            )
        return ArtifactIntakeResult(receipt, True, parser(receipt), None)
