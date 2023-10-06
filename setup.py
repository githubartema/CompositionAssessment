#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from typing import Dict

from setuptools import find_packages, setup

# Package meta-data.
NAME = "samp_net"
REQUIRES_PYTHON = ">=3.8.0"
VERSION = ""

# What packages are required for this module to be executed?
REQUIRED = [  
    'einops==0.3.0',
    'numpy==1.19.1',
    'opencv_contrib_python==4.4.0.46',
    'Pillow==8.4.0',
    'scipy==1.5.2',
    'tensorboardX==2.4',
    'torch==1.10.1',
    'torchvision==0.11.2',
    'tqdm==4.51.0'
]

here = os.path.abspath(os.path.dirname(__file__))

# Load the package's __version__.py module as a dictionary.
about: Dict[str, str] = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

# instruction of data including is in MANIFEST.in file
setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    python_requires=REQUIRES_PYTHON,
    url=about["__url__"],
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=REQUIRED,
    include_package_data=True,
    classifiers=[],
)
