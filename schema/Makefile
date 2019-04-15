.PHONY: FORCE
.SUFFIXES:
.DELETE_ON_ERROR:

YAMLS:=$(wildcard *.yaml)
JSONS:=${YAMLS:.yaml=.json}

all: ${JSONS}

%.json: %.yaml
	./y2j <$< >$@

watch:
	-while true; do ls -1 *.yaml | entr -dn make; done
