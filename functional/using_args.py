# we may choose to pass arguments into a function
# the single asterisk '*' gathers positional arguments
def pos(*args): # any positional arguemnts will be gathered into a tuple called 'args'
    '''this function may recieve zero or more positional arguments'''
    print(type(args)) # tuple
    for i in args:
        print(i)

if __name__ == '__main__':
    pos(4, 5, True, 'ok') # positional arguments
    pos(['hello', 'lunch'], {5,5,5,4,3,2}, False)