BUILD_DIR := build
SOURCES := $(wildcard *-source.yaml)
CLASS_FILTER_FILES = $(SOURCES:%-source.yaml=${BUILD_DIR}/%.classes)
FILTER_CLASSES := $(shell cat ${CLASS_FILTER_FILES})

# Imported class defs (e.g. gkm-core) are generated into def/ from the imported
# source and must be kept. Derive that set from the imported module's json so
# the keep-list stays accurate: if an imported class is removed upstream its
# stale def is pruned too, rather than being kept forever.
IMPORT_CLASSES := $(notdir $(wildcard ../gkm-core/json/*))

FILTER_JSONS = $(FILTER_CLASSES:%=json/%)
FILTER_DEFS = $(FILTER_CLASSES:%=def/%.rst) $(IMPORT_CLASSES:%=def/%.rst)

.DEFAULT: prune

# Prune obsolete generated files: json/ down to this schema's own classes, and
# def/ down to this schema's classes PLUS the imported class defs. This removes
# stale VRS defs (from a renamed/deleted class) while retaining the imported
# gkm-core defs the docs include from def/vrs/.
prune: $(filter-out ${FILTER_JSONS} ${FILTER_DEFS},$(wildcard def/* json/*))
	$(if $^,rm $^)
