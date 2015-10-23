# clilib
A library of emulated command line commands. The goal of this library is to
emulate the most common cammands for Unix and Windows. The primary
use case for this library is in honeypots.

## Setup
Generic install and usage instructions:

### Install
download and extract the latest version from:
run: `python setup.py bdist_egg`
then run: `sudo easy_install dist/clilib-0.0.1-py2.egg`

### Usage
Then add `from clilib import *` to your script.
