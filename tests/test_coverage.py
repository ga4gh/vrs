"""Concrete-class coverage.

Every concrete (instantiable) VRS class -- one whose generated JSON pins a
``type`` const -- must be exercised by at least one *valid* example wired into
``test_definitions.yaml``. This catches a class being added (or renamed) without
any accompanying validation example, which the example-driven tests would
otherwise silently skip.

Add new concrete classes to ``test_definitions.yaml`` (with a valid example),
not to an exemption list here -- ``EXEMPT`` is intentionally empty.
"""
import json

import yaml

from config import root_path, test_path

# Concrete classes that legitimately have no standalone valid instance.
# Keep empty: prefer adding a real example over exempting a class.
EXEMPT: set[str] = set()


def _concrete_vrs_classes():
    """VRS classes whose generated JSON fixes a `type` const (i.e. instantiable)."""
    concrete = set()
    for path in (root_path / "schema" / "vrs" / "json").iterdir():
        schema = json.loads(path.read_text())
        type_prop = schema.get("properties", {}).get("type", {})
        if "const" in type_prop:
            concrete.add(path.stem)
    return concrete


def _classes_with_valid_example():
    spec = yaml.safe_load((test_path / "test_definitions.yaml").read_text())
    return {
        t["definition"]
        for t in spec["tests"]
        if not t.get("shouldValidationFail")
    }


def test_every_concrete_class_has_a_valid_example():
    concrete = _concrete_vrs_classes()
    assert concrete, "expected to discover concrete VRS classes"
    covered = _classes_with_valid_example()
    missing = concrete - covered - EXEMPT
    assert not missing, (
        "concrete VRS classes with no valid example in test_definitions.yaml: "
        f"{sorted(missing)}"
    )
