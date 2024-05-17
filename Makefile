PYV:=3.12
VEDIR=venv/${PYV}

############################################################################
#= SETUP, INSTALLATION, PACKAGING

#=> venv: make a Python 3 virtual environment
.PHONY: venv/%
venv/%:
	python$* -m venv $@; \
	source $@/bin/activate; \
	python -m ensurepip --upgrade; \
	pip install --upgrade pip setuptools

#=> develop: install package in develop mode
.PHONY: develop setup
develop setup:
	pip install -r .requirements.txt

#=> devready: create venv, install prerequisites, install pkg in develop mode
.PHONY: devready
devready:
	make ${VEDIR} && source ${VEDIR}/bin/activate && make develop
	@echo '#################################################################################'
	@echo '###  Do not forget to `source ${VEDIR}/bin/activate` to use this environment  ###'
	@echo '#################################################################################'

############################################################################
#= TESTING
# see test configuration in pyproject.toml

#=> test: execute tests
.PHONY: test
test:
	pytest tests/

#=> doctest: execute documentation tests (requires extra data)
.PHONY: doctest
doctest:
	pytest tests/ --doctest-modules
