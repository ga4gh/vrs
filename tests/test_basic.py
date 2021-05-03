import json

import python_jsonschema_objects as pjs
import yaml

from config import vrs_json_path, vrs_yaml_path


# Are the yaml and json parseable and do they match?
y = yaml.load(open(vrs_yaml_path), Loader=yaml.SafeLoader)
j = json.load(open(vrs_json_path))
assert y == j, "parsed yaml and json do not match"


# Can pjs handle this schema?
ob = pjs.ObjectBuilder("schema/vrs.json")
ob.build_classes()              # no exception => okay
