"""Python setup.py for tmp_pyth package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("tmp_pyth", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="tmp_pyth",
    version=read("tmp_pyth", "VERSION"),
    description="Awesome tmp_pyth created by niski1996",
    url="https://github.com/niski1996/tmp-pyth/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="niski1996",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["tmp_pyth = tmp_pyth.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
