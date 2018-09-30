from math import pi, sqrt


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def area(radius):
        return pi*radius**2


class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    @staticmethod
    def area(side_a, side_b):
        return side_a * side_b


class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @staticmethod
    def area(side_a, side_b, side_c):
        perimeter = side_a+side_b+side_c
        return sqrt((perimeter-side_a)*(perimeter*side_b)*(perimeter*side_c)*perimeter/2)


class Comparison:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value != other.value

    def __ne__(self, other):
        return self.value == other.value
