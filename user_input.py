# we may need to grab data from the user
i = input('Please enter your name: ') # block execution until something is entered
print(type(i)) # ALWAYS a string from 'input'
print(f'Hello {i}')
# we may need to convert the data type (must explicitly assign)
try:
    n = int( float(i) ) # try to convert the string to an integer
    print(n, type(n))
except Exception as err:
    print(err) # we may handle the exception however we choose
finally:
    # this block always runs, whether or not there was an exception
    '''tidy up here...'''

