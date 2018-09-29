import math


def __str__(self):
        return 'I am a %s with area of %d' % (type(self).__name__, self.area())

class Rectangle():
    def __init__(self, base, side):
        self.base = base
        self.side = side
    def area(self):
        return self.base*self.side

class Triangle():
    def __init__(self,base_t,height):
        self.height = height
        self.base_t = base_t
    def area(self):
        return self.base_t*self.height/2

class Triangleside():
    def __init__(self,a,d,c,p):
        self.a = a
        self.d = d
        self.c = c
        self.p = p
    def area(self):
        return  math.sqrt(self.p*(self.p-self.a)*(self.p-self.d)*(self.p-self.c))

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

print('Circle')

r = int(input("Enter radius of circle: "))
obj1 = Circle(r)
print("Area of circle:", round(obj1.area(), 2))


print('Rectangle')

b = int(input("Enter base of rectangle: "))
s=int(input("Enter side of rectangle:"))
obj2=Rectangle(b,s)
print("Area of rectangule:", round(obj2.area(), 2))


print('Triangle')

v = int(input("Enter base of triangle: "))
h = int(input("Enter height of triangle:"))
obj3=Triangle(v,h)
print("Area of triangle:", round(obj3.area(), 2))


print('Triangleside')

a = int(input("Enter side_a triangle: "))
d=int(input("Enter side_d triangle: "))
c = int(input("Enter side_c triangle:"))
p= (a+d+c)/2
obj4 = Triangleside(a,d,c,p)
print("Area of triangle:", round(obj4.area(), 2))




