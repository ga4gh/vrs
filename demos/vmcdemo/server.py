#!/usr/bin/env python

import os

import connexion

if "OPENAPI_SPEC_PATH" not in os.environ:
    raise RuntimeError("Must set OPENAPI_SPEC_PATH")

spec_path = os.path.abspath(os.environ["OPENAPI_SPEC_PATH"])
spec_dir, spec_file = os.path.split(spec_path)

app = connexion.App(__name__, specification_dir=spec_dir)
app.add_api(spec_file)
app.run(port=8080)
