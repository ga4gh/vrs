"""vmcdemo models, defined at runtime from the spec

"""

import sys
import yaml

from bravado_core.spec import Spec

from . import spec_path


spec = Spec(yaml.load(open(spec_path)))
spec.build()

# pull definitions into module namespace
for classname, classdef in spec.definitions.items():
    classdef.__module__ = __name__
    setattr(sys.modules[__name__], classname, classdef)


def unmarshal_Location(d):
    """unmarshal Location object from dictionary d"""
    
    Location(id=d["id"],
             sequence_id=d["sequence_id"],
             
