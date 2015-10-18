import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    long_desc = f.read()

setup(
    name = "clilib",
    version = "0.0.0",
    author = "foospidy",
    author_email = "",
    description = ("Emulates command line commands"),
    license = "GPLv2",
    keywords = "unix windows cli command line",
    url = "https://github.com/foospidy/clilib",
    download_url = "",
    packages = ['clilib'],
    long_description = long_desc,
    classifiers = [
        "Intended Audience :: Honeypots",
        "Topic :: Unix Windows Honeypots :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.7",
        "License :: GPLv2 License",
    ]
)
