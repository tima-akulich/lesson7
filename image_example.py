from PIL import Image

image = Image.open('frog.jpg')

# Вырезаем прямоугольник из картинки
c = image.crop((20, 30, 200, 100))
c.save('frog_crop.jpg')

# Ресайзим картинку
image.thumbnail((400, 200))
image.save('frog_thumb.jpg')
