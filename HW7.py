# Task 1
import argparse
from PIL import Image
import glob
import os
import math


parser = argparse.ArgumentParser()
parser.add_argument('--file', required=True, help='Path for the file')
parser.add_argument('--from-format', required=True, help='json / csv')
parser.add_argument('--to-format', required=True, help='csv / json')
name = parser.parse_args()

# Task 2
print('Size of thumbnail image')

parser1 = argparse.ArgumentParser()
parser1.add_argument('--path', required=True, help='Path to file')
parser1.add_argument('-width', help='Width of image')
parser1.add_argument('-height', help='Height of image')
result = parser1.parse_args()

print('Width of thumbnail image: ', str(result.width))
print('Height of thumbnail image: ', str(result.height))

size = result.width, result.height

for infile in glob.glob(result.path + "/ *.jpg"):
    file, ext = os.path.splitext(infile)
    image = Image.open(infile)
    image.thumbnail(size)
    image.save(file + ".thumbnail", "JPEG")

# Task 3
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
