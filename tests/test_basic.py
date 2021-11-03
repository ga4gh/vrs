import json

import python_jsonschema_objects as pjs
import yaml
from schema.helpers import pjs_filter
from ga4gh.vrsatile.tools.source_proc import YamlSchemaProcessor

from config import vrs_json_path, vrs_yaml_path

# Are the yaml and json parsable and do they match?
y = yaml.load(open(vrs_yaml_path), Loader=yaml.SafeLoader)
p = YamlSchemaProcessor(y)
j = json.load(open(vrs_json_path))


def test_json_yaml_match():
    assert p.for_js == j, "parsed yaml and json do not match"


# Can pjs handle this schema?
def test_pjs_smoke():
    ob = pjs.ObjectBuilder(pjs_filter(y))
    assert ob.build_classes()              # no exception => okay
