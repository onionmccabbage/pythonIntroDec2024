# by convention we often call a module 'main' if it is the 
# entry-point for a collection of Python modules

# we often choose to encapsulate functionality inside a function
# the advantage is we can re-use these functions wehenever needed
# we may choose to pass arguments, and they may have a default value
def validateIsNumeric(v=0): # we may choose to write a DOCSTRING at the top of the fn
    '''take a value and return True is the value is numeric. 
    Otherwise return False'''
    # if(type(v)==int or type(v)==float): # we can say 'and' or 'or'
    if type(v) in (int, float): # does the tyoe exist in the tuple (int, float) ? 
        return True
    else:
        return False
    
def returnWhat():
    '''what does a function return...'''
    if(1==3):
        return 'nonsense' # this will never happen

# exercise the code
r0 = validateIsNumeric() # pass NO args (will fail if there is not a default)
r1 = validateIsNumeric(3) # this overrides the default value
r2 = validateIsNumeric('3')
r3 = validateIsNumeric(3.4)
r4 = validateIsNumeric(-3)
# code clarity matters, so it may be clearer to break code out like this
print( r1 ) # True
print( r2 ) # False
print( r3 ) # True
print( r4 ) # True

print(validateIsNumeric.__doc__) # sometimes it's handy to acess the docstring

r5 = returnWhat()
print(r5) # None
