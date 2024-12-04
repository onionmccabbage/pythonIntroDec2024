# using name mangling and property decorators
# We need to capture a point in 2-d space

class Point:
    '''x and y will specify a point on a plane'''
    def __init__(self, x, y):
        '''property x and y will be numeric values'''
        self.__x = x # __x is called 'name mangling'
        self.__y = y
    def __str__(self):
        '''used by any print() calls'''
        return f'Point is at x:{self.__x} and y:{self.__y}'
    # we may declare property decorators to allow changes to property values
    @property # decorator adds functionality to an existing function
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        '''validate that the incoming new_x is a numeric value'''
        if type(new_x) in (int, float):
            self.__x = new_x
        else:
            raise Exception('X must be numemric')

if __name__ == '__main__':
    p1 = Point(3,4)
    p1.__x = False # we CANNOT directly acces the value of p1.__x
    print(p1.x, p1) # p1.x will call the property function 'x'
