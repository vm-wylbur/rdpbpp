#!/usr/bin/env python
#
# Authors: PB
# Maintainers: PB
# Copyright: 2017, Python Software Foundation License, 2.2 or newer
#
from setuptools import setup, find_packages

setup(
    setup_requires=['pytest-runner'],
    name="rdp",
    version='0.1',
    packages=find_packages(),
    tests_require=['pytest'],
    author='Patrick Ball',
    author_email="pball@hrdag.org",
    description="tools for Real Dumb Parallelism",
    license="PSF",
    url="https://github.com/vm-wylbur/rdpbpp",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
    ],
    scripts=['bin/rdp-init'],
    python_requires='>=3'
)

# done.
