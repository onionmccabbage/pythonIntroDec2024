def readTextFromFile():
    '''retrieve some text from a file'''
    fin = open('my_text.txt', 'rt') # 'rt' will read text
    t = fin.read() # retrieve everything from the file
    fin.close()
    return t

# exercise the code
retreived = readTextFromFile()
print(retreived)

