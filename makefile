.PHONY: build upload

all: build

TEST_PATH=tests

build:
	python3 setup.py sdist
upload:
	twine upload dist/*

test:
	pytest ${TEST_PATH}