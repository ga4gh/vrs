# Variation Representation Specification (VRS)

[![DOI](https://zenodo.org/badge/67005248.svg)](https://zenodo.org/badge/latestdoi/67005248)
[![Read the Docs](https://img.shields.io/readthedocs/vr-spec/1.1)](https://vrs.ga4gh.org/)
[![tests](https://github.com/ga4gh/vrs/actions/workflows/tests.yml/badge.svg)](https://github.com/ga4gh/vrs/actions/workflows/tests.yml)

The [GA4GH](https://www.ga4gh.org/) [Variation Representation Specification](https://vrs.ga4gh.org/)
provides a comprehensive framework for the computational representation of biological sequence
variation. VRS is the result of a collaboration among [contributors](CONTRIBUTORS.md) representing
national information resource providers, major international public initiatives, and diagnostic
testing laboratories.

VRS is licensed under the [Apache License 2.0](LICENSE).

> **NOTE:** VRS is under active development.
> See the [VRS Project Roadmap](https://github.com/orgs/ga4gh/projects/12).

## Specific goals

* Develop common language- and protocol-neutral information models and nomenclature for
  biological sequence variation.
* From the information models, develop data schemas. The current schema is defined in
  JSON Schema, but other formats are expected.
* Provide algorithmic guidance and conventions to minimize representational ambiguity.
* Define a globally unique *computed identifier* for covered data classes.
* Develop [validation tests](./validation/) to ensure consistency of implementations.

The VRS model is the product of the [GA4GH Variation Representation group](https://www.ga4gh.org/product/variation-representation/).

> **SEE ALSO**: See [VRS-Python](https://github.com/ga4gh/vrs-python) for a Python
> implementation and Jupyter notebooks.

## Using the schema

The schema is available in the [schema/](./schema/) directory, in both reStructuredText
(RST) and JSON versions. It conforms to JSON Schema Draft 2020-12. For a list of
libraries that support JSON schema, see
[JSONSchema>Implementations](https://json-schema.org/tools).

## Installing for development

Fork the repo at <https://github.com/ga4gh/vrs>.

    git clone --recurse-submodules git@github.com:YOUR_GITHUB_ID/vrs.git
    cd vrs
    make devready
    source venv/3.12/bin/activate
    pre-commit install

If you already cloned the repo, but forgot to include `--recurse-submodules` you can run:

    git submodule update --init --recursive

## Contributing to the schema

VRS uses [vrs-source.yaml](./schema/vrs/vrs-source.yaml) as the source document for JSON Schema.

To create the corresponding def and json files after making changes to the source document, from the root directory:

    cd schema
    make all

> *Note: We have a custom pre-commit hook to run these commands after you stage a source
> document*

## Contributing to the docs

The VRS specification documentation is written in reStructuredText and located in [docs/source](docs/source/). Commits to this repo are built automatically at <https://vrs.ga4gh.org>.

To build documentation locally, you must install [entr](https://eradman.com/entrproject/):

    brew install entr

Then from the root directory:

    cd docs
    make clean watch &

Then, open [docs/build/html/index.html](./docs/build/html/index.html). The above make
command should build docs when source changes. (Some types of changes require recleaning and building.)

## Testing

The VRS repo contains two kinds of tests. Basic smoke tests in [tests/](./tests/) ensure that the
schema is parsable and works with certain tools. These tests provide a basic sanity
check during development.

Validation tests (in [validation/](./validation/)) provide language-neutral tests for those implementing
tools with VRS.

To run the smoke tests:

    make test
