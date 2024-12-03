def printToFile(t):
    '''send print output to a text file'''
    # we need a file access object
    fout = open('my_text.txt')
    print( t, file=fout ) # print to the file access object


# exercise the code
info = 'this is very simple'
printToFile(info)
