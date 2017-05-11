"""vmcdemo models, defined at runtime from the spec

"""

import os
import sys

import pkg_resources
import python_jsonschema_objects as pjs


schema_dir = pkg_resources.resource_filename(__name__, "_data/schema")
schema_path = schema_dir + "/vmcbundle.json"
schema_file = os.path.basename(schema_path)


builder = pjs.ObjectBuilder(schema_path)
models = builder.build_classes()

# pull definitions into module namespace
for classname in models:
    classdef = getattr(models, classname)
    classdef.__module__ = __name__
    setattr(sys.modules[__name__], classname, classdef)

