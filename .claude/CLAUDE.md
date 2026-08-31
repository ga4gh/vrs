# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

The GA4GH Variation Representation Specification (VRS) — a **schema + documentation** repository, not an application. It defines language-neutral information models for biological sequence variation. There is no runtime library here (the Python implementation lives in the separate `ga4gh/vrs-python` repo); the deliverables are JSON Schema files, generated `.rst` class docs, and a Sphinx documentation site.

## The source-of-truth pipeline (most important thing to understand)

Everything is generated from **`*-source.yaml`** files. **Never hand-edit generated artifacts** — edit the source YAML and regenerate.

- **Source:** `schema/vrs/vrs-source.yaml` is the single source document for the VRS model.
- **Generated from it:**
  - `schema/vrs/json/*` — split JSON Schema, one file per class (no extension).
  - `schema/vrs/def/*.rst` — per-class documentation includes used by the docs.
- **Generator tooling** comes from the `ga4gh.gks.metaschema` pip package (pinned in `.requirements.txt`). The `schema/vrs/Makefile` invokes its console scripts: `source2classes`, `source2splitjs` (JSON), and `y2t` (rst def files). You will not find these scripts in this repo.

To regenerate after editing source YAML:

```bash
cd schema && make all      # iterates every schema/<name>/ subdir, runs its Makefile
# or narrower:
cd schema/vrs && make all
cd schema/vrs && make clean # wipes build/, json/, def/ — regenerate after
```

A **pre-commit hook** (`pre-commit-hooks/update-json-def-files.sh`, wired in `.pre-commit-config.yaml`) runs `make all` and auto-stages regenerated `json/`+`def/` files whenever a `*-source.yaml` is committed. Similar hooks regenerate `examples/` and `validation/` outputs. Because of this, forgetting to run `make` locally is usually caught at commit time — but only if `pre-commit install` was run.

## The gkm-core submodule

`schema/vrs/vrs-source.yaml` **imports shared base classes** (e.g. `Entity`, `Element`, `Extension`, `iriReference`, `MappableConcept`) from the core-schema git submodule:

```yaml
imports:
  gkm-core: ../gkm-core/gkm-core-source.yaml
namespaces:
  gkm.core: /ga4gh/schema/gkm-core/<version>/json/
```

- `inherits: gkm-core:Entity` and `$refCurie: gkm.core:iriReference` in the source YAML resolve through this submodule.
- The generated VRS JSON files contain `$ref`s into `/ga4gh/schema/gkm-core/<version>/json/...`.
- **Naming note (rebrand):** the upstream GitHub repo was renamed from `gks-core` to **`gkm-core`** (Genomic Knowledge Models), so the schema tree, source file, `$id`/`$ref` namespace, the git submodule *path* (`submodules/gkm-core`), and the remote (`github.com/ga4gh/gkm-core.git`) all use `gkm-core` now. The submodule tracks the `1.2.0-ballot.2026-07` branch. `schema/gkm-core` and `docs/source/def/gkm-core` are symlinks into `submodules/gkm-core/schema/gkm-core`.
- Consequence: the pinned submodule commit and the `<version>` string in the namespace/`$ref`s must stay in sync. Bumping the core version means updating both the submodule pointer **and** the version strings in `vrs-source.yaml`, then regenerating.
- Always clone with `--recurse-submodules` (or `git submodule update --init --recursive`), or the build cannot resolve imports.

## Setup

```bash
make devready                       # creates venv/3.12, installs .requirements.txt
source venv/3.12/bin/activate
pre-commit install                  # strongly recommended — keeps generated files in sync
```

## Tests

Two distinct kinds:

- **Smoke tests** — `tests/` (`make test` → `pytest tests/`). Confirm the schema parses and loads with tooling; `test_examples.py` validates `examples/` against the schema. Fast sanity check. Run a single test with `pytest tests/test_basic.py::<name>`.
- **Validation tests** — `validation/` (`models.yaml`, `functions.yaml`). Language-neutral conformance fixtures for implementers, not a pytest suite.

## Docs

Sphinx / reStructuredText under `docs/source/`, published to https://vrs.ga4gh.org. Prose pages are hand-written; per-class `def/*.rst` are generated (see pipeline above). Live-build locally:

```bash
brew install entr
cd docs && make clean watch &      # open docs/build/html/index.html
```

## Editing conventions

- To change the model: edit `schema/vrs/vrs-source.yaml`, run `cd schema && make all`, and commit both source and regenerated `json/`+`def/` together.
- To change examples: edit `examples/*.yaml` (the hook regenerates `examples/json/` and the examples README).
- `$id`/version strings appear in many generated files; they originate from the source YAML header and the gkm-core namespace — change them at the source, not in the generated output.
