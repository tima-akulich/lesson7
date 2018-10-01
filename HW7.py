# Task 1
import argparse
from PIL import Image
import glob
import os


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


