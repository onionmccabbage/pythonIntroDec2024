# maybe we need a utility to provide a random integer between 0-100
from random import randint

def num0_100():
    '''return a random integer between 0-100 inclusive'''
    n = randint(0,100)
    return n