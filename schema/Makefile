.PHONY: defs FORCE
.SECONDARY:
.SUFFIXES:
.DELETE_ON_ERROR:

JSYAMLS:=vrs.yaml
JSONS:=${JSYAMLS:.yaml=.json}

all: ${JSONS} defs

%.json: %.yaml
	jsy2js.py <$< >$@

%.yaml: %-source.yaml
	source2jsy.py $< >$@

defs:
	rm -rf defs
	y2t.py vrs-source.yaml

## # npm install -g json-dereference-cli
## %.json: %.yaml
## 	json-dereference -s $< -o $@


watch:
	-while true; do ls -1 *.yaml | entr -dn make ${JSONS}; done
