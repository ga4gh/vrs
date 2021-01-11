.PHONY: FORCE
.SUFFIXES:
.DELETE_ON_ERROR:

YAMLS:=$(wildcard *.yaml)
JSONS:=${YAMLS:.yaml=.json}

all: ${JSONS} vrs.json

%.json: %.yaml
	./y2j <$< >$@

vrs.json: vr.json
	cp vr.json vrs.json

## # npm install -g json-dereference-cli
## %.json: %.yaml
## 	json-dereference -s $< -o $@


watch:
	-while true; do ls -1 *.yaml | entr -dn make vr.json; done
