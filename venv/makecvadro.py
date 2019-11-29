from PIL import Image
import os

#получает картинку вписывает ее в квадрат минимально возможной стороыны

def new_jpgsuqare(name, nameold):
    im = Image.open(nameold)
    pixels = im.load()
    width, height = im.size

    ns = max(width, height)
    new_image = Image.new("RGB", (ns, ns), color=(255, 255, 255))
    pixelsn = new_image.load()

    for i in range((ns - width) // 2, (ns - width) // 2 + width):
        for j in range((ns - height) // 2, (ns - height) // 2 + height):
            pixelsn[i, j] = pixels[i - (ns - width) // 2, j - (ns - height) // 2]

    new_image.save(name, "JPEG", quality=95)


for file in os.listdir():
    if file.endswith(".jpg"):
        new_jpgsuqare(file.split(".")[0] + "2.jpeg", file)
