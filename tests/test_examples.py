from config import test_dir, schema_dir, examples_dir
import yaml
from jsonschema import validate


def get_schema(schema_file, schema_class, kw="$defs"):
    return {
      "$ref": schema_dir.as_uri() + f"/{schema_file}.json#/{kw}/{schema_class}"
    }


def test_examples():
    with open(test_dir / 'test_definitions.yaml') as def_file:
        test_spec = yaml.safe_load(def_file)
    for test in test_spec['tests']:
        with open(examples_dir / test['test_file']) as datafile:
            data = yaml.safe_load(datafile)
        schema = get_schema(
            test['schema'],
            test['definition'],
            test.get('kw', '$defs')
        )
        assert validate(data, schema) is None
