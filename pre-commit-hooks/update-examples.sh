#!/bin/bash

REPO_ROOT=$(git rev-parse --show-toplevel)
EXAMPLES_DIR="$REPO_ROOT/examples"

cd "$EXAMPLES_DIR" || exit 1

make all

if git diff --quiet json/ README.md; then
  echo "No changes to source files in $EXAMPLES_DIR."
else
  echo "Source files updated in $EXAMPLES_DIR, adding changes to commit."
  git add $(git ls-files --modified json/ *.yaml README.md)
fi

exit 0
