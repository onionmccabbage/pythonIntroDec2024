def cleanup(*args):
    '''if there is one argument, validate it as numeric
    If there are two arguments validate they are the same type
    for three arguments return them in a tuple'''
    if len(args)==1:
        if type(args[0]) in (int, float):
            return args[0]
        else:
            return 1 # just retrun a sensible default value
    elif len(args)==2:
        if type(args[0]) == type(args[1]):
            return args # just return the arguments
        else:
            raise Exception('Types need to be the same')
    elif len(args)==3:
        return args
    else:
        '''we should consider what to do for other outcomes'''

if __name__ == '__main__':
    print( cleanup(3) ) # all good
    print( cleanup('3') ) # 1
    print( cleanup('3', '4') ) # all fine
    print( cleanup('a', 'b', 'c') ) # all fine
    print( cleanup('3', 4) ) # exception

