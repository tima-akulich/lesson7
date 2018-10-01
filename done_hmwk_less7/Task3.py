class Circle():
    def __init__(self, r):
        self.r = r
    def sqr(self):
        import math
        return math.pi*self.r**2

class Rectangle():
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def sqr(self):
        return self.h*self.w

class Triangle():
    def __init__(self ,a ,b ,c):
        self.a = a
        self.b = b
        self.c = c
    def sqr(self):
        p=(a+b+c)/2
        return sqrt(p*(p-a)(p-b)(p-c))