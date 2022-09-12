import json

import python_jsonschema_objects as pjs
import yaml
from schema.helpers import pjs_filter
from ga4gh.gks.metaschema.tools.source_proc import YamlSchemaProcessor

from config import vrs_json_path, vrs_yaml_path, vrs_merged_yaml_path

# Are the yaml and json parsable and do they match?
p = YamlSchemaProcessor(vrs_yaml_path)
j = json.load(open(vrs_json_path))


def test_json_yaml_match():
    assert p.for_js == j, "parsed yaml and json do not match"


# Can pjs handle this schema?
def test_pjs_smoke():
    ob = pjs.ObjectBuilder(pjs_filter(j))
    assert ob.build_classes()              # no exception => okay
