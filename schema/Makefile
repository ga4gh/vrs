.PHONY: FORCE
.SUFFIXES:
.DELETE_ON_ERROR:

YAMLS:=vrs.yaml
JSONS:=${YAMLS:.yaml=.json}

all: ${JSONS} defs

%.json: %.yaml
	./y2j.py <$< >$@

## # npm install -g json-dereference-cli
## %.json: %.yaml
## 	json-dereference -s $< -o $@


watch:
	-while true; do ls -1 *.yaml | entr -dn make ${JSONS}; done
