#! /usr/bin/env python3

from setuptools import setup, find_packages

setup(name="mscz",
    version="0.0.1",
    license="GPL-v3",
    author="Guillaume W. Bres",
    author_email="guillaume.bressaix@gmail.com",
    keywords="parser",
    install_requires=["lxml"],
    packages=find_packages("mscz"),
    py_modules = ["mscz/mscz"],
)
