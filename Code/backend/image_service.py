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
    side_length = 0

    if (image.Image.width > image.Image.height):
        side_length = image.Image.width
    else:
        side_length = image.Image.height
    
    new_image = image.resize((side_length, side_length))
    return new_image


# This method resizes an image to given width and height
def resize_image(image, width, height):
    new_image = image.resize((width, height))
    return new_image

# This method will print given points on an image by coordinates
def print_points_on_image(image, points):
    print(image)

