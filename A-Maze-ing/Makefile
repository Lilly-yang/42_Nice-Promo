install:

run:
    python3 a_maze_ing.py config.txt

debug:

clean:
    rm -f 

lint:
    flake8 .
    mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
    flack8 .
    mypy . --strict