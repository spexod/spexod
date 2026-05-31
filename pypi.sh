#!/bin/bash
# build and twine are PyPI tooling
pip install --upgrade pip build twine

# ensure the distribution directory exists.
mkdir dist

# clean out old artifacts so you don't upload stale builds
rm -rf dist/*

# build both wheel and sdist into dist/
python -m build

# verify the metadata is valid before uploading
python -m twine check dist/*

# # upload to test PyPI
# python -m twine upload --repository testpypi dist/*
# # testpypi installation
# pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple spexod==0.3.0

# upload to PyPI
python -m twine upload --repository pypi dist/*
# # PyPI installation
# pip install spexod