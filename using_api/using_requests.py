import requests # remember we may need to pip install requests
# for python 2 we would import urllib3 which works differently

# We may need to access data from an external API (Application Programming Interface)
# These tend to exist as URLs also REST (REspresent STate)

def getAllUsers():
    '''Make a requests to an API to retrieve all users'''
    apiUrl = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(apiUrl) # here we make a call to the URL and grab the response
    # this particular API will return JSON data
    data = response.json()
    return data

# exercise the code
r = getAllUsers()
print(r, type(r))

