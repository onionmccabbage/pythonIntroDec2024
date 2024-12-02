# a dictionary is a useful collection type
# it is like an objec,t or a hash in other languages
# it is a non-ordinal, mutable collection of key:value pairs
d = {'name':'Floella', 'age':72, 'level':'admin', 'current':True, 'skills':('Python', 'Bash')}
print(type(d), d)
# we may access members of a dictionary
print(d['skills'])
# we can mutate and add to the dict
d['current'] = False
d['additional'] = [5,4,3,2]
print(d) # NB do not rely on the order of the members - they are NOT ordinal

# we may iterate over a dict (even though it is not ordinal)
for k in d:
    print(k) # we have the keys

for (k,v) in d.items(): # NB we MUST say d.items() if we need key and value
    # print(k, v)
    print(f'key {k} has value {v}')

# NB identifiers are case-sensitive

# string formatting
s1 = 'menu'
s2 = 'fish'
# we may inject any Python onto {}
print(f'On the {s1} is {s2}') # f'' means format this string
# other syntax
print('On the {0} is {1}'.format(s1, s2)) # older syntax
