# if you need to persist data do this
a=1
# if you need a bunch of related data, use a structure
t = ('Ethel', 42, 'admin', 'porrige')
# maybe a dict
d = {'n':'Ethel', 'age':42, 'sec':'admin', 'brek':'porrige'}
# there is no way for enforce the data type in structures
d['sec'] = False # oops - we need a string or a validated value

# a class lets us combine data structures with validation logic
class ThatsClever():
    def __init__(n, a, s, b):
        '''here we can validate the parameters to make sure they are ok'''



