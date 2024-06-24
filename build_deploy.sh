#!/bin/zsh

rm -rf dist build *.egg-info

source .venv/bin/activate
python3 -m md-rst README.md README.rst
python3 setup.py clean --all install clean --all
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*.tar.gz dist/*.whl