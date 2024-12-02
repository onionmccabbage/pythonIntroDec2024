# comments look like this
# we declare identifiers using letters, numbers, underscore (don't start with a digit)
a = 3 # integer
b = 7.2 # float

print( type(a), type(b) )
# we may carry out mathematical operations
print( a+b, a-b, b/a ) # python will type convert where possible. e.g. float/int is a float
print(b**a) # ** here means raise to the power
print(b//a) # integer division (modulo)
print(b%a)  # remainder division

# other data types (NB Python is not data type safe)
a = True # or False the identifier 'a' now points to a memory location containing a boolean
n = None # can be handy

# other data types
# string may be in single quotes, double quotes, triple quotes, triple double quotes
s = """hello and welcome to Python
preserver new lines             tabs etc.""" # a string of characters
t = 'we may encode new line \n and tab \t within quotes'
# string are an immutable ordinal collection of characters
s = 'changed' # we are not mutating the string, we are creationg sa new string
# we may access members of the string using 'slicing'
print(  )

