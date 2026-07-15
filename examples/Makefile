.SECONDARY:
.DELETE_ON_ERROR:
.PHONY: README.md

BUILD_DIR := build
YAML_DIR := .
JSON_DIR := json

vpath %.tag $(BUILD_DIR)

SOURCES := $(wildcard $(YAML_DIR)/*.yaml)
TAGS := $(notdir $(SOURCES:.yaml=.tag))

all: $(BUILD_DIR) $(TAGS) README.md

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(JSON_DIR):
	mkdir -p $(JSON_DIR)

%.tag: $(YAML_DIR)/%.yaml | $(JSON_DIR) $(BUILD_DIR)
	@python -c "import sys, yaml, json; json.dump(yaml.safe_load(sys.stdin), sys.stdout, indent=2)" \
		< $< > $(JSON_DIR)/$*.json
	@echo "" >> $(JSON_DIR)/$*.json
	@touch $(BUILD_DIR)/$@

README.md: $(TAGS)
	@python generate_readme.py

clean:
	rm -f $(BUILD_DIR)/*.tag
	rm -f $(JSON_DIR)/*.json
	rm -f README.md
