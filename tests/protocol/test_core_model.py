from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parents[2] / "packages" / "protocol-model"))

from odop_model import CanonicalRightReference, RightRecord, RightsObjectRecord


def test_right_references_are_scoped_to_the_owning_rights_object() -> None:
    record = RightsObjectRecord.from_rights(
        object_id="object-a",
        asset_reference={"external": "opaque"},
        rights=[RightRecord("right-1"), RightRecord("right-2")],
    )

    assert record.canonical_references() == (
        CanonicalRightReference("object-a", "right-1"),
        CanonicalRightReference("object-a", "right-2"),
    )


def test_asset_reference_remains_an_opaque_model_value() -> None:
    reference = object()
    record = RightsObjectRecord.from_rights("object-a", reference, [])

    assert record.asset_reference is reference
