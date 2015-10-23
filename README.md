# clilib
A library of emulated command line commands. The goal of this library is to
emulate the most common cammands for Unix and Windows. The primary
use case for this library is in honeypots.

## Setup
Install and usage instructions (tested on Debian Linux):

### Install
clone this project or download and extract the latest version from: https://github.com/foospidy/clilib/releases and `cd` into the project directory.

run: `python setup.py bdist_egg`

then run: `sudo easy_install -Z dist/clilib-0.0.1-py2.egg`

### Usage
Import clilib into your script with `from clilib import *`

