.PHONY: defs vrs.xml FORCE
.SECONDARY:
.SUFFIXES:
.DELETE_ON_ERROR:

JSYAMLS:=vrs.yaml
JSONS:=${JSYAMLS:.yaml=.json}

all: vrs.json vrs.xml defs

vrs.json: vrs.yaml
	jsy2js.py <$< >$@

vrs.yaml: vrs-source.yaml
	source2jsy.py <$< >$@

vrs.xml: vrs.json
	@python3 -c "from json2xml import json2xml; from json2xml.utils import readfromjson; data = readfromjson('vrs.json'); file = open('vrs.xml', 'w'); file.write(json2xml.Json2xml(data).to_xml()); file.close();"

defs:
	rm -rf defs
	y2t.py vrs-source.yaml

## # npm install -g json-dereference-cli
## %.json: %.yaml
## 	json-dereference -s $< -o $@


watch:
	-while true; do ls -1 *.yaml | entr -dn make ${JSONS}; done
