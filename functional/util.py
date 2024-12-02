# maybe we need a utility to provide a random integer between 0-100
from random import randint

def num0_100():
    '''return a random integer between 0-100 inclusive'''
    n = randint(0,100)
    return n

# put this in a separate module then import it
def validateIsNumeric(v=0): # we may choose to write a DOCSTRING at the top of the fn
    '''take a value and return True is the value is numeric. 
    Otherwise return False'''
    # if(type(v)==int or type(v)==float): # we can say 'and' or 'or'
    if type(v) in (int, float): # does the tyoe exist in the tuple (int, float) ? 
        return True
    else:
        return False