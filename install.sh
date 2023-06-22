#!/bin/bash
git submodule update --init
cp config.yaml.example config.yaml
python3 setup.py sdist
mkdir dist
pip install dist/*.tar.gz
rm -rf dist
rm -rf *.egg-info
echo "pseudo installed! Run 'pseudo' to start the program."
