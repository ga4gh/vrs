import json
from ga4gh.gks.metaschema.tools.source_proc import YamlSchemaProcessor
import pytest

from config import vrs_source_path, validator, root_path


@pytest.fixture(scope="module")
def json_schema():
    """Create test fixture for JSON schema"""
    schemas = {}
    json_schema_dir = root_path / "schema" / "vrs" / "json"

    for path in json_schema_dir.iterdir():
        with open(path) as f:
            schemas[path.stem] = json.load(f)

    return schemas



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


def load_all_json_schemas():
    schemas = {}

    for path in (root_path / "schema" / "vrs" / "json").iterdir():
        with open(path) as f:
            schema = json.load(f)

        class_name = path.stem
        schemas[class_name] = schema
    return schemas


def test_ga4gh_inherent_properties_exist(json_schema):
    for class_name, schema in json_schema.items():
        ga4gh_block = schema.get("ga4gh", {})
        inherent = ga4gh_block.get("inherent")

        if not inherent:
            continue

        class_properties = set(schema.get("properties", {}).keys())
        missing = set(inherent) - class_properties

        assert not missing, (
            f"{class_name} ga4gh.inherent properties not found in properties: {missing}"
        )


def test_type_property_matches_class_name(json_schema):
    for class_name, schema in json_schema.items():
        properties = schema.get("properties", {})

        if "type" not in properties:
            continue

        type_prop = properties["type"]
        const_value = type_prop.get("const")
        assert const_value

        default_value = type_prop.get("default")
        assert default_value

        assert default_value == const_value

        assert const_value == class_name, (
            f"{class_name} has mismatched type const: expected '{class_name}', got '{const_value}'"
        )
