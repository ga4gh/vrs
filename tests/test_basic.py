import json

import yaml
import python_jsonschema_objects as pjs
from schema.helpers import pjs_filter
from ga4gh.gks.metaschema.tools.source_proc import YamlSchemaProcessor
from jsonschema import validate, RefResolver

from config import vrs_json_path, vrs_yaml_path, root_dir

# Are the yaml and json parsable and do they match?
p = YamlSchemaProcessor(vrs_yaml_path)
j = json.load(open(vrs_json_path))


def test_json_yaml_match():
    assert p.for_js == j, "parsed yaml and json do not match"


# Can pjs handle this schema?
def test_pjs_smoke():
    ob = pjs.ObjectBuilder(pjs_filter(j))
    assert ob.build_classes()              # no exception => okay


def test_schema_validation():
    """Test that examples in validation/models.yaml are valid"""
    resolver = RefResolver.from_schema(j, store={"definitions": j})
    schema_definitions = j["definitions"]
    validation_models = root_dir / "validation" / "models.yaml"
    validation_tests = yaml.load(open(validation_models), Loader=yaml.SafeLoader)
    for cls, tests in validation_tests.items():
        for t in tests:
            validate(instance=t["in"],
                     schema=schema_definitions[cls],
                     resolver=resolver)
