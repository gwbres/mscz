#! /usr/bin/env python3

try:
    from setuptools import setup
    from setuptools import find_namespace_packages
except ImportError:
    from distutils.core import setup

setup(name="mscz",
    version="0.0.1",
    license="GPL-v3",
    author="Guillaume W. Bres",
    author_email="guillaume.bressaix@gmail.com",
    keywords="parser",
    install_requires=["lxml"],
    packages=find_namespace_packages(include=["mscz"]),
    package_dir = {"mscz": "mscz"},
)
