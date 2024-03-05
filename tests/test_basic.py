import json

import jsonschema as js
from ga4gh.gks.metaschema.tools.source_proc import YamlSchemaProcessor

from config import vrs_source_path, validator

# Is the YAML parseable?
p = YamlSchemaProcessor(vrs_source_path)


def test_yaml_process():
    assert p.for_js, "processor loads and processes yaml"


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
    validator['SequenceLocation'].validate(sl)

    a = {
        'location': sl,
        'state': {
            'type': 'ReferenceLengthExpression',
            'length': [32, 35],
            'repeatSubunitLength': 3
        },
        'type': 'Allele'
    }
    validator['Allele'].validate(a)
