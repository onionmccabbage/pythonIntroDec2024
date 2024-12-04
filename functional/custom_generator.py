import datetime
# a generator is an efficient mechanism to yield values in a sequence
# the built in generator works like this
g = (i**3 for i in range(-10, 11))

# we can write our own genersator function
def genTimestamp():
    '''This function will yield a date-timestamp of todays date and time'''
    while True:
        now = datetime.datetime.now() # we havea date time object represent 'now'
        ds  = now.strftime('%d-%m-%Y %H:%M:%S')
        yield ds # the yield makes this function into a generator

if __name__ == '__main__':
    # we need an instance of our custom generator
    ts_g = genTimestamp()
    print( type(ts_g) )
    print( ts_g.__next__() ) # access the next member yielded by a generator
    for i in g:
        print(i)    
    print( ts_g.__next__() ) # access the next member yielded by a generator

