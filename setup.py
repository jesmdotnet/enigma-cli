# setup.py
from setuptools import setup

setup(
    name="enigma-cli",
    version="0.1.0",
    py_modules=["enigma", "main"],
    entry_points={
        "console_scripts": [
            "enigma-cli=main:main",
        ],
    },
    install_requires=[],
    author="Jesse Mullavey",
    description="CLI Enigma Machine emulator",
)
