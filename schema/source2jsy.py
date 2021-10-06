#!/usr/bin/env python3

import yaml
import sys
from source_proc import YamlSchemaProcessor

raw_schema = yaml.load(sys.stdin, Loader=yaml.SafeLoader)
p = YamlSchemaProcessor(raw_schema)
p.js_yaml_dump(sys.stdout)
