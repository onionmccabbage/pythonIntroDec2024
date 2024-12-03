# we may specify an absolute path
# or you can derive a path from sys.path, sys.cwd etc.

def printToFile(t):
    '''send print output to a text file'''
    try:
        # we need a file access object
        # for exclusive file access, use 'xt' which will create the file, or throw an exception
        fout = open('my_text.txt', 'at') # 'at' will create or append text ('t' is the default)
        print( t, file=fout ) # print to the file access object
    # handle specific exceptions
    except FileNotFoundError as err:
        print(f'Problem: {err}')
    # then handle any generic exceptions
    except Exception as err:
        print(f'Some other problem occured: {err}')

# exercise the code
info = 'this is very simple'
printToFile(info)
