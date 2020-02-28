.PHONY: build upload

all: build

build:
	python3 setup.py sdist
upload:
	twine upload dist/*