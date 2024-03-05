from pathlib import Path
import json
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
from jsonschema import Draft202012Validator
import re

root_dir = Path(__file__).parent.parent
schema_dir = root_dir / "schema"
test_dir = root_dir / "tests"
examples_dir = root_dir / "examples"
vrs_source_path = schema_dir / "vrs" / "vrs-source.yaml"
vrs_jsons_path = schema_dir / "vrs" / "json"


ga4gh_re = re.compile(r'.*\/ga4gh\/schema\/([\w\-\.]+)\/[\w\.]+\/(.*)$')


def retrieve_rel_ref(ga4gh_ref: str):
    ga4gh_match = ga4gh_re.match(ga4gh_ref)
    if ga4gh_match is None:
        raise ValueError(f'ga4gh_ref {ga4gh_ref} is not a root GA4GH reference')
    schema_module = ga4gh_match.group(1)
    local_path = ga4gh_match.group(2)
    resolved_path = (schema_dir / schema_module / local_path).resolve()
    schema = json.loads(resolved_path.read_text())
    return Resource.from_contents(schema)


vrs_js_registry = Registry(retrieve=retrieve_rel_ref)
vrs_js = dict()
vrs_validator = dict()

for schema_path in vrs_jsons_path.glob('*'):
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