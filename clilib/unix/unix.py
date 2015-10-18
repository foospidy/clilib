from uname import *
from rm import *
from echo import *

def man(*params):
  if None == params:
    return "Error!"
  elif not params or not params[0]:
    return 'What manual page do you want?'
  else:
    command = params[0]
    return eval(command[0]).__doc__
