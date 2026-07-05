from PIL import Image
import os

def conv_ascii(image_path: str, charset: str):

    img=Image.open(image_path)
    img=img.convert("L")

    t_width = os.get_terminal_size().columns
    img_width = img.width
    img_height = img.height

    scale = t_width / img_width
    new_width = t_width
    new_height = int(img_height * scale * 0.5)

    dims = (new_width, new_height)

    img = img.resize(dims)

    pixels = img.getdata()

    end = []
    for pixel in pixels:
       index = pixel * (len(charset) - 1) // 255
       end.append(charset[index])

    for y in range(new_height):
            row = end[y * new_width : (y + 1) * new_width]
            print("".join(row))