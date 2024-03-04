from pathlib import Path
import json
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
from jsonschema import Draft202012Validator

root_dir = Path(__file__).parent.parent
schema_dir = root_dir / "schema"
test_dir = root_dir / "tests"
examples_dir = root_dir / "examples"
vrs_yaml_path = schema_dir / "vrs-source.yaml"
vrs_jsons_path = schema_dir / "json"


def retrieve_rel_ref(rel_ref: str):
    resolved_path = (vrs_jsons_path / rel_ref).resolve()
    schema = json.loads(resolved_path.read_text())
    return Resource.from_contents(schema)


vrs_js_registry = Registry(retrieve=retrieve_rel_ref)
vrs_js = dict()
vrs_validator = dict()

for schema_path in vrs_jsons_path.glob('*.json'):
    content = json.loads(schema_path.read_text())
    schema_uri = schema_path.as_uri()
    content['id'] = schema_uri
    schema_resource = Resource(contents=content, specification=DRAFT202012)
    vrs_js[schema_path.stem] = content
    vrs_schemas = vrs_js_registry.with_resources([
        (schema_path.name, schema_resource),
        (schema_uri, schema_resource)
    ])

for cls in vrs_js:
    vrs_validator[cls] = Draft202012Validator(vrs_js[cls], registry=vrs_js_registry)
