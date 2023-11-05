from facial_keypoint import Position
from binascii import a2b_base64
from PIL import Image
import base64

def convert_dataurl_to_image(data_url):
    print(data_url)
    binary_data = a2b_base64(data_url)
    with open('image.png', 'wb') as f:
        f.write(binary_data)
        img = Image.open('./image.png')
        return img
    
    


# This method resizes an image to have even sides
def normalize_image(image: Image):
    width, height = image.size
    side_length = 0

    if (width > height):
        side_length = height
    else:
        side_length = width
    
    new_image = image.resize((side_length, side_length))
    return new_image


# This method resizes an image to given width and height
def resize_image(image, width, height):
    new_image = image.resize((width, height))
    return new_image

# This method will print given points on an image by coordinates
def print_points_on_image(image, points):
    print(image)


def get_average_pixels(image, width, height):
    pixels = image.load()
    average_pixels = []

    for x in range(width):
        for y in range(height):
            pixel = pixels[x, y]
            sum = 0
            for val in pixel:
                sum +=val

            average_pixels.append(sum//len(pixel))

    return average_pixels
