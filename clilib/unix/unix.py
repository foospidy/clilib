from uname import *
from echo import *

def man(command=None):
	if None == command or '' == command.strip():
		return "What manual page do you want?"
	else:
		return eval(command).__doc__
	