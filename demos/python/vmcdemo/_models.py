"""vmcdemo models, defined at runtime from the spec

**This file should not be imported directly.**

vmcdemo.__init__ exports all symbols for external users. Please see
that file.

"""

import os

import pkg_resources
import python_jsonschema_objects as pjs


schema_dir = pkg_resources.resource_filename(__name__, "_data/schema")
schema_path = schema_dir + "/vmcbundle.json"
schema_file = os.path.basename(schema_path)


builder = pjs.ObjectBuilder(schema_path)
models = builder.build_classes()
