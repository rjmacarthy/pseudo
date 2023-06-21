from setuptools import setup

setup(
    name='pseudo',
    version='1.0',
    py_modules=['pseudo'],
    entry_points={
        'console_scripts': [
            'pseudo = pseudo:main',
        ],
    },
)