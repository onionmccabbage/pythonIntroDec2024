from class_b import Point

# class inheritance
class Point3D(Point):
    '''This 3-d point inherits from 2-d point'''
    def __init__(self, x, y, z):
        '''call the __init__ of the parent class'''
        super().__init__(x, y)
        self.z = z # additional properties for this class
    # method: a function belonging to the class
    def hypot(self): # this is a derived value (no need to persist we can alsways derive it)
        '''find the hypotenuse of x and y
        h=sqrt(x*x+y*y)'''
        h = (self.x**2+self.y**2)**0.5 # raise to 0.5 is the square root
        return h

if __name__ == '__main__':
    p3a = Point3D(-3, -4, 5)
    print(p3a)
    print(f'The hypotenuse of {p3a} is {p3a.hypot()}')