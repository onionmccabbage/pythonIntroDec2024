# by convention we often call a module 'main' if it is the 
# entry-point for a collection of Python modules

# we often choose to encapsulate functionality inside a function
# the advantage is we can re-use these functions wehenever needed
def validateIsNumeric(v): # we may choose to write a DOCSTRING at the top of the fn
    '''take a value and return True is the value is numeric. 
    Otherwise return False'''
    try:
        if(type(v)==int or type(type(v)==float)): # we can say 'and' or 'or'
            return True
    except Exception as err:
        return False

# exercise the code
print( validateIsNumeric(3) )   # True
print( validateIsNumeric('3') ) # False
print( validateIsNumeric(3.4) ) # True
print( validateIsNumeric(-3) )  # True

print(validateIsNumeric.__doc__) # sometimes it's handy to acess the docstring

