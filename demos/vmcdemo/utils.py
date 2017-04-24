import yaml

from bravado_core.spec import Spec


class ModelBucket:
    pass


def build_models(fn):
    """return *dict* of models from the given yaml file"""
    spec = Spec(yaml.load(open(fn)))
    spec.build()
    models = ModelBucket()
    for classname, classdef in spec.definitions.items():
        setattr(models, classname, classdef)
    return models
