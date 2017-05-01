"""vmcdemo models, defined at runtime

"""

import sys
import yaml

from bravado_core.spec import Spec
import pkg_resources


spec_dir = pkg_resources.resource_filename(__name__, "_data/spec")
vmc_spec_fn = spec_dir + "/vmc.yaml"
spec = Spec(yaml.load(open(vmc_spec_fn)))
spec.build()
for classname, classdef in spec.definitions.items():
    classdef.__module__ = __name__
    setattr(sys.modules[__name__], classname, classdef)
