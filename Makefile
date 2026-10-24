PYTHON := $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)
EX ?= 01
.PHONY: test check notebooks verify

test:
	$(PYTHON) -m pytest -q

check:
	$(PYTHON) -m pytest -q tests/test_ex$(EX).py

notebooks:
	$(PYTHON) scripts/validate_notebooks.py

verify:
	USE_SOLUTIONS=1 $(PYTHON) -m pytest -q
	$(PYTHON) scripts/verify_starters.py
	$(PYTHON) scripts/validate_notebooks.py
