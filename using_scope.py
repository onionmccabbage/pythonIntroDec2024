# data always exists within a scope
# the 'global' scope is anything not inside a code block
# any data declared in a code block is scoped to that code block

def fnA():
    '''this function is a code block so it has its own local scope'''
    a = 'local'
    return a
# can we know the scope at runtime??????

def fnB():
    global a # we now have access the the variable 'a' from the global scope
    a = 'changed'

a = 'global' # a variable in the global scope (not inside any code block)

if __name__ == '__main__':
    '''exercise the code'''
    print( fnA() ) # 'local'
    print( a ) # 'global'
    fnB()
    print( a ) # 'changed