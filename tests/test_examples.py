from config import test_path, examples_path
import yaml
from config import validator
from pytest import raises
from jsonschema.exceptions import ValidationError
from contextlib import nullcontext

def test_examples():
    with open(test_path / 'test_definitions.yaml') as def_file:
        test_spec = yaml.safe_load(def_file)
    for test in test_spec['tests']:
        with open(examples_path / test['test_file']) as datafile:
            data = yaml.safe_load(datafile)
        class_validator = validator[test['definition']]
        
        try:
            with raises(ValidationError) if test.get("shouldValidationFail") else nullcontext():
                assert class_validator.validate(data) is None
        except AssertionError as e:
            raise AssertionError(f"AssertionError in {test['test_file']}: {e}")
