#!/bin/bash

REPO_ROOT=$(git rev-parse --show-toplevel)
VALIDATION_DIR="$REPO_ROOT/validation"

cd "$VALIDATION_DIR" || exit 1

make all

if git diff --quiet json/; then
  echo "No changes to source files in $VALIDATION_DIR."
else
  echo "Source files updated in $VALIDATION_DIR, adding changes to commit."
  git add $(git ls-files --modified json/ *.yaml)
fi

exit 0
