from pathlib import Path

root_dir = Path(__file__).parent.parent
schema_dir = root_dir / "schema"
vrs_yaml_path = schema_dir / "vrs-source.yaml"
vrs_json_path = schema_dir / "vrs.json"
vrs_merged_yaml_path = schema_dir / "merged.yaml"

