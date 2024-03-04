from pathlib import Path

root_dir = Path(__file__).parent.parent
schema_dir = root_dir / "schema"
test_dir = root_dir / "tests"
examples_dir = root_dir / "examples"
vrs_yaml_path = schema_dir / "vrs-source.yaml"
vrs_jsons_path = schema_dir / "json"

