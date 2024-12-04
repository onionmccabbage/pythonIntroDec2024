# we may choose to pass arguments into a function
# the single asterisk '*' gathers positional arguments
# NB *args must come AFTER any existing explicit positional arguments
def pos(x, *args): # any extra positional argumemnts will be gathered into a tuple called 'args'
    '''this function may recieve zero or more positional arguments'''
    print(type(args)) # tuple
    for i in args:
        print(i)

def k(**kwargs):
    '''here any keyword arguments will be gathered into a dict called 'kwargs' '''
    print(type(kwargs))
    for k, v in kwargs.items():
        print(k, v)

if __name__ == '__main__':
    pos(4, 5, True, 'ok') # positional arguments
    pos(['hello', 'lunch'], {5,5,5,4,3,2}, False)
    #
    k(x=3, y=9, j=[], l=pos ) # keyword arguments always specify something=value