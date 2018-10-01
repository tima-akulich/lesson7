import argparse
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('--path', dest='p', required=True,
                        type=str, help='way to path with pics')
parser.add_argument('--width', dest='w',
                        type=int, help='width of thumbnail')
parser.add_argument('--height', dest='h',
                        type=int, help='height of thumbnail')
result = parser.parse_args()

from PIL import Image
import os
import re
Images = []
for root, dirs, files in os.walk(result.p):
    for filename in files:
        Images.append(re.findall(r'\b\w+.jpg\b', filename))

for item in Images:
    if item:
        image = Image.open(item[0])
        image.thumbnail((result.w, result.h))
        image.save(item[0].replace('.jpg', '_thumb.jpg'))
