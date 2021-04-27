.PHONY: FORCE
.SUFFIXES:
.DELETE_ON_ERROR:

YAMLS:=ga4gh.yaml vrs.yaml
JSONS:=${YAMLS:.yaml=.json}
PROTOS:=vrs.proto

all: ${JSONS} ${PROTOS}

%.json: %.yaml
	./y2j <$< >$@

%.proto: %.yaml
	./y2p <$< >$@

## # npm install -g json-dereference-cli
## %.json: %.yaml
## 	json-dereference -s $< -o $@


watch:
	-while true; do ls -1 *.yaml | entr -dn make ${JSONS}; done
