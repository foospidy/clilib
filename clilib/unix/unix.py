from uname import *
from rm import *
from echo import *
from whoami import *
from which import *

def man(command=None):
  if None == command or '' == command:
    return 'What manual page do you want?'
  else:
    return eval(command).__doc__
