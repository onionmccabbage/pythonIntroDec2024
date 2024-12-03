import json # this tool lets us convert between json text and Python structures

# NB JSON insists on double quotes
j_t = '{"name":"Freda", "age":42}' # this is plain text
d   = json.loads(j_t) # json.loads() will try to convert json text into a python structure
print(d, type(d))
# we can convert back to json text
r   = json.dumps(d) # json.dumps() will convert the structure into json text
print(r, type(r))
