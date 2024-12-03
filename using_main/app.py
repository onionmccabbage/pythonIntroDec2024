from util import MethA
# CAREFUL - when we import from a module, any immediate code is executed
from other import MethB

def fnC():
    return 'function C'

# exercise the code
print( MethA() ) 
print( MethB() ) 
print( fnC() )

# what does Python consider to be __name__
if __name__ == '__main__':
    print(__name__)