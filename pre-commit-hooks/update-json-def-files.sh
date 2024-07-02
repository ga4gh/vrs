#!/bin/bash

REPO_ROOT=$(git rev-parse --show-toplevel)
SCHEMA_DIR="$REPO_ROOT/schema"
DIRS=$(find "$SCHEMA_DIR" -mindepth 1 -maxdepth 1 -type d | sort)

for DIR in $DIRS; do
  cd "$DIR" || exit 1

  make_output=$(make all)

  if [[ "$make_output" == "make: Nothing to be done for \`all\'." ]]; then
    echo "No changes to source files in $DIR."
  else
    echo "Source files updated in $DIR, adding changes to commit."
    git add $(git ls-files --modified json def)
  fi
done

exit 0
