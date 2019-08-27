import setuptools
from pathlib import Path


setuptools.setup(
    name="vinpdf",
    version=1.0,
    long_description=Path("readme.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "data"])
)
