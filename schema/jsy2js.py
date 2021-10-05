#!/usr/bin/env python3

import yaml
import json
import sys

yaml_schema = yaml.load(sys.stdin, Loader=yaml.SafeLoader)
json.dump(yaml_schema, sys.stdout, indent=3)
