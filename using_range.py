# the range object is very efficient
n = 5
odds = range(1, 10, 2) # more efficient
is_odd = n in odds
evens = [0, 2, 4, 6, 8, 10] # less efficient
is_even = n in evens

# we may even do maths within a range (this is then called comprehension)
squares_lists = [i*i for i in range(0,11)] # we now have a list containing squares 0-10
print(squares_lists, type(squares_lists))

# The generator syntax
# a generator is even more eficient than a range/list
g = (i*i for i in range(0,11)) # we now have a generator (the values are NOT stored in memory)
print( g, type(g) )
# we may itersate over the members of the generator
for i in g:
    print(i)