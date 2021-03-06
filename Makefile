.PHONY: all environment install install-mac install-linux install-windows lint validate test test-example coverage coverage-html coverage-xml coverage-erase

CODE_COVERAGE ?= 80
WINDOWS_32BIT_GMPY2 ?= packages/gmpy2-2.0.8-cp38-cp38-win32.whl
WINDOWS_64BIT_GMPY2 ?= packages/gmpy2-2.0.8-cp38-cp38-win_amd64.whl
OS ?= $(shell python -c 'import platform; print(platform.system())')
IS_64_BIT ?= $(shell python -c 'from sys import maxsize; print(maxsize > 2**32)')

all: environment install validate lint coverage

requirements.txt: Pipfile
	pip freeze > requirements.txt

environment:
	@echo 🔧 PIPENV SETUP
	pip install pipenv
	python -m pipenv install --dev

install:
	@echo 📦 Install Module
	@echo Operating System identified as $(OS)
ifeq ($(OS), Linux)
	make install-linux
endif
ifeq ($(OS), Darwin)
	make install-mac
endif
ifeq ($(OS), Windows)
	make install-windows
endif
ifeq ($(OS), Windows_NT)
	make install-windows
endif

install-mac:
	@echo 🍎 MACOS INSTALL
# gmpy2 requirements
	brew install gmp || true
# install module
	pipenv run python -m pip install -e .

install-linux:
	@echo 🐧 LINUX INSTALL
# gmpy2 requirements
	sudo apt-get install libgmp-dev
	sudo apt-get install libmpfr-dev
	sudo apt-get install libmpc-dev
# install module
	pipenv run python -m pip install -e .

install-windows:
	@echo 🏁 WINDOWS INSTALL
# install module with local gmpy2 package
ifeq ($(IS_64_BIT), True)
	pipenv run python -m pip install -f $(WINDOWS_64BIT_GMPY2) -e . 
endif
ifeq ($(IS_64_BIT), False)
	pipenv run python -m pip install -f $(WINDOWS_32BIT_GMPY2) -e . 
endif

black:
	black apps src tests setup.py

lint:
	@echo 💚 LINT
	@echo 1.Pylint
	pipenv run pylint .
	@echo 2.Black Formatting
	pipenv run black --check .
	@echo 3.Mypy Static Typing
	pipenv run mypy apps src tests setup.py
	@echo 4.Package Metadata
	pipenv run python setup.py check --strict --metadata --restructuredtext
# 	@echo 5.Docstring
# 	pipenv run pydocstyle

validate: 
	@echo ✅ VALIDATE
	@pipenv run python -c 'import electionguard; print(electionguard.__package__ + " successfully imported")'

test: 
	@echo ✅ TEST
	pipenv run pytest . -x

coverage:
	@echo ✅ COVERAGE
	pipenv run coverage run -m pytest
	pipenv run coverage report --fail-under=$(CODE_COVERAGE)

coverage-html:
	pipenv run coverage html -d coverage

coverage-xml:
	pipenv run coverage xml

coverage-erase:
	@pipenv run coverage erase

upgrade-electionguard:
	pipenv uninstall electionguard
	pipenv install -e 'git+https://github.com/microsoft/electionguard-python.git@feature/generic_chaum_petersen#egg=electionguard'
#	pipenv install -e 'git+https://github.com/microsoft/electionguard-python.git#egg=electionguard'
