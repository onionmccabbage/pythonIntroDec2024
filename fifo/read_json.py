# we will read JSON text from a file (a text file)
# then convert to a Python structure (in this case a list of dict)
# then show the results iteratively (a loop)
import json # part of the standard python library

def readData():
    '''read in JSON from a text file'''
    fin = open('todos.json', 'rt')
    retreived = fin.read() # read the whole file in
    fin.close()
    return retreived

def convert(d):
    '''convert the json 'd' into a Python structure'''
    s = json.loads(d)
    return s

def prettyPrint(s):
    '''iterate over a structure to show the results nicely'''
    if type(s) == dict:
        for (k,v) in s:
            print(f'{k}:{v}')
    elif type(s) == list:
        for i in s:
            print(f'{i}')


# exercise the code