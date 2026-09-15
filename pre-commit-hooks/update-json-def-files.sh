#!/bin/bash

REPO_ROOT=$(git rev-parse --show-toplevel)
SCHEMA_DIR="$REPO_ROOT/schema"
DIRS=$(find "$SCHEMA_DIR" -mindepth 1 -maxdepth 1 -type d | sort)

for DIR in $DIRS; do
  # Skip import-only schema dirs (e.g. schema/gkm-core: a real directory holding
  # only symlinks to an imported source + json, with no Makefile). There is
  # nothing to generate there, and running make would error.
  if [ ! -f "$DIR/Makefile" ]; then
    echo "Skipping $DIR (no Makefile — import-only)."
    continue
  fi

  cd "$DIR" || exit 1

  # Fail loudly if generation fails (e.g. missing deps on a clean runner) rather
  # than silently swallowing the error and exiting 0 -- that would let the CQA
  # check falsely pass without validating the regenerated output.
  if ! make_output=$(make all); then
    echo "ERROR: 'make all' failed in $DIR" >&2
    echo "$make_output" >&2
    exit 1
  fi

  if [[ "$make_output" == "make: Nothing to be done for \`all\'." ]]; then
    echo "No changes to source files in $DIR."
  else
    echo "Source files updated in $DIR, adding changes to commit."
    git add $(git ls-files --modified json def)
  fi
done

exit 0
