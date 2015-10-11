import os
import sys

sys.dont_write_bytecode = True

UNIX    = {'posix', 'mac'}
WINDOWS = {'nt'}

if os.name in UNIX:
	print "unix"
	from unix import *
elif os.name in WINDOWS:
	print "windows"
	from windows import *
else:
	print "Error!"
