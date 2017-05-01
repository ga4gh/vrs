import os

import pkg_resources


spec_dir = pkg_resources.resource_filename(__name__, "_data/spec")
spec_path = spec_dir + "/vmc.yaml"
spec_file = os.path.basename(spec_path)
