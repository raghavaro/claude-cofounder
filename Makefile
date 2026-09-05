# Rebuild everything generated from the modules. Run after adding or editing
# a file under flows/ or references/.
.PHONY: all check

all:
	python3 scripts/build_express.py
	python3 scripts/build_index.py
	python3 portable/build.py
	python3 scripts/build_skill_zip.py

check:
	python3 scripts/build_express.py --check
	python3 scripts/build_index.py --check
	python3 portable/build.py --check
	python3 scripts/build_skill_zip.py --check
	python3 -m unittest discover -s tests
