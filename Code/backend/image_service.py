from facial_keypoint import Position
from binascii import a2b_base64
from PIL import Image
import base64
import matplotlib.pyplot as plt

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
    print(width)
    print(height)
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
    fig = plt.figure(frameon=False)
    for i in range(len(points)//2):
        x = points[i]
        y = points[i + 1]
        plt.plot(x, y, marker='o', color="red") 

    plt.axis('off') 
    plt.autoscale(True)
    plt.imshow(image) 
   
    # plt.show()
    plt.savefig('augmented.png', bbox_inches='tight')


def vis_im_keypoint_notstandard(img, points, axs): # same function as before but deals with keypoints when they are not standardized
  # fig = plt.figure(figsize=(6, 4))
  print(points)
  axs.imshow(img.reshape(96, 96))
  for point in points:
      print(point)

  xcoords = (points[0::2] + 0.)
  ycoords = (points[1::2] + 0.) 
  axs.scatter(xcoords, ycoords, color='red', marker='o')




def get_average_pixels(image, width, height):
    pixels = image.load()
    average_pixels = []

    for x in range(width):
        for y in range(height):
           
            pixel = pixels[y, x]
            sum = 0
            counter = 0
            for val in pixel:
                sum +=val
            average_pixels.append(sum//len(pixel))
    return average_pixels
