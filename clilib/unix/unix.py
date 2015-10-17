from uname import *
from rm import *
from echo import *

def man(command=None):
  if None == command:
    print "Error!"
  else:
    print eval(command).__doc__
