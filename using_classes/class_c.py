from class_b import Point

# class inheritance
class Point3D(Point):
    '''This 3-d point inherits from 2-d point'''

if __name__ == '__main__':
    p3a = Point3D(-3, -4)
    print(p3a)