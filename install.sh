git submodule update --init
python setup.py sdist
pip install dist/*.tar.gz
rm -rf dist
rm -rf *.egg-info
echo "pseudo installed! Run 'pseudo' to start the program."
