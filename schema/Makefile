.PHONY: defs FORCE
.SECONDARY:
.SUFFIXES:
.DELETE_ON_ERROR:

JSYAMLS:=vrs.yaml core.yaml
JSONS:=${JSYAMLS:.yaml=.json}

all: ${JSONS} merged.json defs

%.json: %.yaml
	jsy2js.py <$< >$@

%.yaml: %-source.yaml
	source2jsy.py $< >$@

merged.yaml: vrs-source.yaml
	source2mergedjsy.py $< >$@

defs:
	rm -rf defs
	y2t.py vrs-source.yaml
	y2t.py core-source.yaml

## # npm install -g json-dereference-cli
## %.json: %.yaml
## 	json-dereference -s $< -o $@


watch:
	-while true; do ls -1 *.yaml | entr -dn make ${JSONS}; done
