import pillow as image

img = image.Image("luther.jpg")

print(img.getWidth())
print(img.getHeight())

p = img.getPixel(30, 100)
print(p)
print(p.getRed(), p.getGreen(), p.getBlue())
