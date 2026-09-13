PYTHON = python3
MAIN = a_maze_ing.py

.PHONY: install run debug clean lint lint-strict conda

install:
	$(PYTHON) -m pip install flake8 mypy

run:
	$(PYTHON) $(MAIN) config.txt

debug:
	$(PYTHON) -m pdb $(MAIN) config.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	fing . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

lint:
	flake8 .
	mypy . --warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs

lint-strict:
	flack8 .
	mypy . --strict

conda:
	@echo "Use": conda activate python42
