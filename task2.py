import argparse
import glob
import os

from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('--path', required=True, type=str)
parser.add_argument('--width', required=True, type=int)
parser.add_argument('--height', required=True, type=int)
image_thumb = parser.parse_args()

os.chdir(image_thumb.path)

for i in glob.glob("*.jpg"):
    image = Image.open(i)
    image.thumbnail((image_thumb.width, image_thumb.height))
    image.save('Thumb_'+i)
