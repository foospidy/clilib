import os
from setuptools import setup


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))

    return paths

extra_files = package_files('clilib/')
here        = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    long_desc = f.read()

setup(
    name = "clilib",
    version = "0.0.1",
    author = "foospidy",
    author_email = "",
    description = ("Emulates command line commands"),
    license = "GPLv2",
    keywords = "unix windows cli command line",
    url = "https://github.com/foospidy/clilib",
    download_url = "",
    packages = ['clilib'],
    package_data = {'': extra_files},
    long_description = long_desc,
    classifiers = [
        "Intended Audience :: Honeypots",
        "Topic :: Unix Windows Honeypots :: Libraries :: Python Modules",
        "Programming Language :: Python :: 2.7",
        "License :: GPLv2 License",
    ]
)
