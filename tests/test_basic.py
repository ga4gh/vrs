import copy
import json

import jsonschema as js
import yaml
from ga4gh.gks.metaschema.tools.source_proc import YamlSchemaProcessor

from config import vrs_json_path, vrs_yaml_path, vrs_merged_yaml_path

# Are the yaml and json parsable and do they match?
p = YamlSchemaProcessor(vrs_yaml_path)
j = json.load(open(vrs_json_path))
m = yaml.safe_load(open(vrs_merged_yaml_path))


def test_json_yaml_match():
    assert p.for_js == j, "parsed yaml and json do not match"


def test_all_value_objects_with_digest_keys():
    for pc in p.processed_classes:
        if p.class_is_abstract(pc) or p.class_is_primitive(pc) or not p.class_is_subclass(pc, 'ValueObject'):
            continue
        pc_properties = set(p.defs[pc]['properties'].keys())
        try:
            pc_digest_keys = set(p.defs[pc]['ga4ghDigest']['keys'])
        except KeyError:
            if p.defs[pc]['ga4ghDigest']['assigned']:
                continue
            raise KeyError(f'{pc} has no keys defined.')
        assert pc_digest_keys <= pc_properties


# Does the schema validate against a simple sequence location?
def test_simple_sequence_location():
    sl = {
        'sequenceReference': {
            'refgetAccession': 'SQ.9W6SPR3RMCHWCSGJLQHE6KBOD285V5SW',
            'type':'SequenceReference'
        },
        'start': 100,
        'end': [None, 150],
        'type': 'SequenceLocation'
    }
    schema = copy.deepcopy(j)
    schema['$ref'] = '#/$defs/SequenceLocation'
    schema['$id'] = vrs_json_path.as_uri()
    js.validate(sl, schema)

    schema['$ref'] = '#/$defs/Allele'
    a = {
        'location': sl,
        'state': {
            'type': 'ReferenceLengthExpression',
            'length': [32, 35],
            'repeatSubunitLength': 3
        },
        'type': 'Allele'
    }
    js.validate(a, schema)
