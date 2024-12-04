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

if __name__ == '__main__':
    p1 = Point(3,4)
    p1.__x = False # we CANNOT directly acces the value of p1.__x
    print(p1.__x, p1)
