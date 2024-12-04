# using name mangling and property decorators
# We need to capture a point in 2-d space

class Point:
    '''x and y will specify a point on a plane
    They are valiated, and raise exceptinos if not valid'''
    __slots__ = ['__x', '__y'] # a list of the only permitted properties for this class
    def __init__(self, x, y):
        '''property x and y will be numeric values'''
        self.x = x # call x setter method
        self.y = y 
    def __str__(self):
        '''used by any print() calls'''
        return f'Point is at x:{self.__x} and y:{self.__y}'
    # we may declare property decorators to allow changes to property values
    @property # decorator adds functionality to an existing function
    def x(self): # this is a getter (or an accessor)
        return self.__x
    @x.setter
    def x(self, new_x): # this is a setter (or a mutator)
        '''validate that the incoming new_x is a numeric value'''
        if type(new_x) in (int, float):
            self.__x = new_x
        else:
            raise Exception('X must be numemric')
    @property # CAREFUL only ONE property decorator per function
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y): 
        '''validate that the incoming new_y is a numeric value'''
        if type(new_y) in (int, float):
            self.__y = new_y # __y is called 'name mangling'
        else:
            raise Exception('Y must be numemric')

if __name__ == '__main__':
    p1 = Point(3,4)
    print(p1.__doc__) # acess the docstring of the class
    # p1.__x = False # we CANNOT directly acces the value of p1.__x
    print(p1.x, p1) # p1.x will call the property function 'x'
