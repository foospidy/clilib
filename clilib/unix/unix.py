from uname import *

def man(command=None):
	if None == command:
		print "Error!"
	else:
		print eval(command).__doc__
	