import requests # remember we may need to pip install requests
import sys
# for python 2 we would import urllib3 which works differently

# We may need to access data from an external API (Application Programming Interface)
# These tend to exist as URLs also REST (REspresent STate)

def getAllUsers():
    '''Make a requests to an API to retrieve all users'''
    apiUrl = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(apiUrl) # here we make a call to the URL and grab the response
    # this particular API will return JSON data
    data = response.json() # or response.xml, response.text response.html ...
    return data # a list of dict objects

def getOneUser(n='1'): # n will default to '1' but that can be overriden by any function call
    '''Make a request including a parameter to indicate which user we want'''
    n = str(n) # make sure n is a string
    if n.isnumeric(): # isnumeric will check if a string value is a number (no . no -)
        apiUrl = f'https://jsonplaceholder.typicode.com/users/{n}'
        response = requests.get(apiUrl)
        # Python will convert the JSON text into a Python structure (dict or list)
        singleUser = response.json() # we call the json() function
        return singleUser # a dict
    else:
        return 'nothing found - we need a numeric value'

# exercise the code
r = getAllUsers()
print(r, type(r))
# get one user
# check to see if there are additional system arguments
if len(sys.argv)>1:
    id = sys.argv[1] # grab the argument
    s = getOneUser(id)
else:
    s = getOneUser() # pass no ID (use the default)
# s = getOneUser('broken')
print(s, type(s))

