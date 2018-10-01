import argparse
from PIL import Image
import os


parser = argparse.ArgumentParser()
parser.add_argument('--path', required=True, type=str)
parser.add_argument('--width', required=True, type=int)
parser.add_argument('--height', required=True, type=int)
r = parser.parse_args()

files = os.listdir(r.path)
images = filter(lambda x: x.endswith('.jpg'), files)

for i in images:
    j = Image.open(i)
    j.thumbnail((r.width, r.height))
    j.save(i.replace('.jpg', '-edited.jpg'))
