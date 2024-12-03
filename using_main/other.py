def MethB():
    return 'Method B'
# any code outside a code block is considered 'immediate' code (will run on import of this module)
if __name__ == '__main__':
    print( f'other says {MethB()}' )
    # this is interesting
    # when any module is run directly, __name__ will be '__main__'
    print(f'module is called {__name__}')