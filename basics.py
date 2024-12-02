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
print( s[0], t[7] ) # 'c' 'e'
print( t[3:6] ) # 'may' [start:stop-before:step]
# we may also choose to iterate over a collection
for i in s: # the colon indicates the beggining of a code block
    j=3
    k='this is indented so it forms part of the current code block'
    print(i) # this line is indented because it belongs to the code block

# when the lines are no longer indented, that is the end of the code block

# some other collection data-types: list and tuple
# NB when we populate a list it may be by value or by reference
l = [3, 8.444, 'coffee', False, s, a, [t, 5]] # this is a list: a mutable ordinal non-sparse collection of any data type
l[4]='other'
print(l[0:6:2]) # [start:stop-before:step]
v = (5, 3, 9, 'immutable', None) # an immutable non-sparse ordinal collection of any data type
print(type(l), type(v), v, v[4])
# v[3] = 'no can do' # we cannot mutate members of a tuple
# we may append, insert, pop or remove with a list
l.append(v) # NB a complex structure will be isntered by reference
l.insert(3, 'inserted at 3')
l.pop() # removed the last member
l.remove('other') # remove a specific value
print(l)
# we may itersate over a list or tuple
