#!/usr/bin/env python

import sys
import yaml

from bravado.client import SwaggerClient

if __name__ == "__main__":
    fn = sys.argv[1]
    client = SwaggerClient.from_spec(yaml.load(open(fn)))
