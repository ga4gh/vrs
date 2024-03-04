from config import test_dir, schema_dir, examples_dir
import yaml
from config import vrs_validator


def get_validator(schema_file, schema_class):
    validator = globals()[f'{schema_file}_validator'][schema_class]
    return validator


def test_examples():
    with open(test_dir / 'test_definitions.yaml') as def_file:
        test_spec = yaml.safe_load(def_file)
    for test in test_spec['tests']:
        with open(examples_dir / test['test_file']) as datafile:
            data = yaml.safe_load(datafile)
        validator = get_validator(
            test['schema'],
            test['definition']
        )
        try:
            assert validator.validate(data) is None
        except AssertionError as e:
            raise AssertionError(f"AssertionError in {test['test_file']}: {e}")
