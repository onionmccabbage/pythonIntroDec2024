# we may need to grab data from the user
i = input('Please enter a number: ') # block execution until something is entered
print(type(i)) # ALWAYS a string from 'input'
print(f'Hello {i}')
# we may need to convert the data type (must explicitly assign)
try:
    n = int( float(i) ) # try to convert the string to an integer
    print(n, type(n))
except Exception as err: # Except is a keyword. We assign to any arbitrary variable, such as 'err'
    # we might try something different, or try again, or log the error....
    print(err) # we may handle the exception however we choose
finally:
    # this block always runs, whether or not there was an exception
    '''tidy up here...'''

# conditional logic
# here, if the number is less than zero, we get the positive part
# if the number is 0-100, we square
# for larger numbers we ignore...
if (type(n==int) and n<0):
    r = abs(n) # n*-1
elif (n>100): # elif is optional
    r = 'we only deal with numbers 0-100'
else: # else is optional
    r = n**2
