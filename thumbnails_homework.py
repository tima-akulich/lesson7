import glob
from PIL import Image
print('SIZE_Thumbnail_image')
w=int(input('width:'))
h=int(input('height:'))
for image_path in glob.glob("*.jpg"):
  im = Image.open(image_path)
  im.thumbnail((w,h), Image.ANTIALIAS)
  if image_path[0:2] != "Th_":
    im.save("Th_" + image_path, "JPEG")







