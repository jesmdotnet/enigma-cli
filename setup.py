from setuptools import setup

setup(
    name='enigma-cli',
    version='0.1',
    py_modules=['enigma', 'main'],
    entry_points={
        'console_scripts': [
            'enigma-cli = main:main',
        ],
    },
)
