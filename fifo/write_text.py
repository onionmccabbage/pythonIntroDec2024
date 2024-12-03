# we may specify an absolute path
# or you can derive a path from sys.path, sys.cwd etc.

def printToFile(t):
    '''send print output to a text file'''
    try:
        # we need a file access object (ask the OS to manage the file system)
        # for exclusive file access, use 'xt' which will create the file, or throw an exception
        fout = open('my_text.txt', 'at') # 'at' will create or append text ('t' is the default)
        # NB every 'print' statement adds a new line character by default
        print( t, file=fout ) # print to the file access object
        # remember to tidy up when done
        fout.close() # this makes the resource available for garbage collection
    # handle specific exceptions
    except FileNotFoundError as err:
        print(f'Problem: {err}')
    # then handle any generic exceptions
    except Exception as err:
        print(f'Some other problem occured: {err}')

def writeToFile(t):
    '''Write the text to a text file without using print'''


# exercise the code
info = 'this is very simple'
printToFile(info)
