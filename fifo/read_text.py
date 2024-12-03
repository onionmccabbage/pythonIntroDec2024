def readTextFromFile():
    '''retrieve some text from a file'''
    fin = open('my_text.txt', 'rt') # 'rt' will read text
    # t = fin.read() # retrieve everything from the file
    t = fin.readlines() # retrieve everything into a list of strings (each line)
    fin.close()
    return t

# exercise the code
retreived = readTextFromFile()
print(retreived, type(retreived))

