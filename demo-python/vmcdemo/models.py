"""vmcdemo models, defined at runtime

"""

import sys
import yaml

from bravado_core.spec import Spec

from . import spec_path


spec = Spec(yaml.load(open(spec_path)))
spec.build()
for classname, classdef in spec.definitions.items():
    classdef.__module__ = __name__
    setattr(sys.modules[__name__], classname, classdef)
