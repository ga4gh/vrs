BUILD_DIR := build
SOURCES := $(wildcard *-source.yaml)
CLASS_FILTER_FILES = $(SOURCES:%-source.yaml=${BUILD_DIR}/%.classes)
FILTER_CLASSES := $(shell cat ${CLASS_FILTER_FILES})
FILTER_JSONS = $(FILTER_CLASSES:%=json/%)
FILTER_DEFS = $(FILTER_CLASSES:%=def/%.rst)

.DEFAULT: prune

prune: $(filter-out ${FILTER_JSONS} ${FILTER_DEFS},$(wildcard def/* json/*))
	$(if $^,rm $^)
