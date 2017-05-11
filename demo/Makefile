.SUFFIXES:
.DELETE_ON_ERROR:
.PHONY: FORCE

export OPENAPI_SPEC_PATH=$(realpath ../spec/vmc.yaml)

default:
	@echo "Ain't no $@ target" 1>&2; exit 1

venv: FORCE
	rm -fr $@
	pyvenv $@
	. $@/bin/activate; pip install -U -r reqs

start-server:
	python -m vmcdemo.server



.PHONY: clean cleaner cleanest
clean:
	find . \( -name \*~ -o -name \*.bak \) -print0 | xargs -0r /bin/rm
cleaner: clean
	find . -name __pycache__ -print0 | xargs -0r /bin/rm -fr
cleanest: cleaner
