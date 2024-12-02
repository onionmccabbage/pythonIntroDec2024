# there is a standard library of features that copme with Python
from random import randint
# we will ask the user for a number, validate and compare to collections

a = (1,2,3,4)
b = [5,6,7,8]
c = randint(-10, 10) # a random integer between these facets

# we can loop endlessly using 'while'
while True:
    '''careful - this will NEVER end!!!!'''
    s = input('Please enter a number: ')
    try:
        n = int(float(s))
        if n in a:
            print(f'{n} is in {a}')
        break # stops the while loop
    except:
        print('we need an integer, try again')

print(f'By the way, the random integer was {c}')