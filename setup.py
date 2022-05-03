import os
import re
import setuptools

HERE = os.path.dirname(os.path.abspath(__file__))


def get_version():
    filename = os.path.join(HERE, 'respect_validation', '__init__.py')
    with open(filename) as f:
        contents = f.read()
    pattern = r"^__version__ = '(.*?)'$"
    return str(re.search(pattern, contents, re.MULTILINE).group(1))


with open("README.md", "r") as fh:
    long_description = re.sub(re.compile(r'<p align="center">.*</p>', re.S), '', str(fh.read()))

setuptools.setup(
    version=get_version(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages('.', exclude=("doc", "examples", "bin", "tests*")),
    # packages=["respect_validation"],
    py_modules=["respect_validation"],
)