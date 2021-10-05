.PHONY: defs FORCE
.SUFFIXES:
.DELETE_ON_ERROR:

YAMLS:=vrs.yaml
JSONS:=${YAMLS:.yaml=.json}

all: vrs.json defs

vrs.json: vrs.yaml
	./jsy2js.py <$< >$@

vrs.yaml: vrs-source.yaml
	./source2jsy.py <$< >$@

defs:
	rm -rf defs
	./y2t.py

## # npm install -g json-dereference-cli
## %.json: %.yaml
## 	json-dereference -s $< -o $@


watch:
	-while true; do ls -1 *.yaml | entr -dn make ${JSONS}; done
