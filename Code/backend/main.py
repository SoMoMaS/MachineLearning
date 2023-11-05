from ast import List
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from facial_keypoint import FacialKeyPoints, Position

from image_service import convert_dataurl_to_image, normalize_image, resize_image, print_points_on_image, get_average_pixels

import tensorflow as tf
import numpy as np

from PIL import Image

#from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware

class Picture(BaseModel):
    pixels: list = []
    data_url: str


# Load models
ml_model_10_epochs = tf.keras.models.load_model('./Models/10/facial_keypoint_model_10_epochs.keras')
ml_model_50_epochs = tf.keras.models.load_model('./Models/50/facial_keypoint_model_50_epochs.keras')
ml_model_100_epochs = tf.keras.models.load_model('./Models/100/facial_keypoint_model_100_epochs.keras')


app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:8000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"], expose_headers=["*"])

@app.get("/facialkeypoints/epochs_10")
async def get_facial_keypoints(picture: Picture) -> FacialKeyPoints:
    formatedPixels = preparePixelData(picture.pixels, 96, 96)
    predicted_points = ml_model_10_epochs.predict(formatedPixels)[0]
    facialKeypoints = convertToFacialKeypoints(predicted_points)
    return facialKeypoints

@app.get("/facialkeypoints/epochs_50")
async def get_facial_keypoints(picture: Picture):
    formatedPixels = preparePixelData(picture.pixels, 96, 96)
    predicted_points = ml_model_50_epochs.predict(formatedPixels)[0]
    facialKeypoints = convertToFacialKeypoints(predicted_points)
    return facialKeypoints

@app.get("/facialkeypoints/epochs_100")
async def get_facial_keypoints(picture: Picture):
    formatedPixels = preparePixelData(picture.pixels, 96, 96)
    predicted_points = ml_model_100_epochs.predict(formatedPixels)[0]
    facialKeypoints = convertToFacialKeypoints(predicted_points)
    return facialKeypoints


@app.get("/facialkeypoints/dataurl")
async def get_facial_keypoints_by_data_url(picture: Picture):
    image = convert_dataurl_to_image(picture.data_url)
    normalized_image = normalize_image(image) # resized to same sides 
    shrunk_image = resize_image(normalize_image, 96, 96) # Resized image to 96x96

    pixels = np.asarray(shrunk_image)
    print(len(pixels))
    formatedPixels = preparePixelData(pixels)

    predicted_points = ml_model_100_epochs.predict(formatedPixels)[0]
    facialKeypoints = convertToFacialKeypoints(predicted_points)
    return facialKeypoints

@app.post("/facialkeypoints/raw")
async def get_facial_keypoints_by_raw_image(picture: Picture):

    # Convert the pixels into an array using numpy
    array = np.array(picture.pixels, dtype=np.uint8)
    formatted = np.reshape(array, (480, 640, 4))
    image = Image.fromarray(formatted)
    image.save('original.png')

    normalized_image = normalize_image(image) # resized to same sides 
    normalized_image.save('normalized.png')

    shrunk_image = resize_image(normalized_image, 96, 96) # Resized image to 96x96
    shrunk_image.save('shrunk.png')

    avarage_pixels = get_average_pixels(shrunk_image, 96, 96)


    formatedPixels = preparePixelData(avarage_pixels, 96, 96)
    predicted_points = ml_model_100_epochs.predict(formatedPixels)[0]
    facialKeypoints = convertToFacialKeypoints(predicted_points)

    return facialKeypoints

def preparePixelData(pixels, width, height):
    data = []
    test_imgs_arr = np.array(pixels, dtype='float')
    test_imgs_arr = np.reshape(test_imgs_arr, (1, width, height, 1))
    data = test_imgs_arr/255.
    
    return data

def convertToFacialKeypoints(predicted_points):
    facialKeyPoints = FacialKeyPoints()

    positions = []
    for i in range(len(predicted_points)//2):
       
        x = predicted_points[i]
        y = predicted_points[i + 1]
        position = Position(x_Coordinate = x, y_Coordinate = y)
        positions.append(position)
        i += 2
    print(positions)
    facialKeyPoints.left_eye_center = positions[0]
    facialKeyPoints.right_eye_center = positions[1]
    facialKeyPoints.left_eye_inner_corner = positions[2]
    facialKeyPoints.left_eye_outer_corner = positions[3]
    facialKeyPoints.right_eye_inner_corner = positions[4]
    facialKeyPoints.right_eye_outer_corner = positions[5]
    facialKeyPoints.left_eyebrow_inner_end = positions[6]
    facialKeyPoints.left_eyebrow_outer_end = positions[7]
    facialKeyPoints.right_eyebrow_inner_end = positions[8]
    facialKeyPoints.right_eyebrow_outer_end = positions[9]
    facialKeyPoints.nose_tip = positions[10]
    facialKeyPoints.mouth_left_corner = positions[11]
    facialKeyPoints.mouth_right_corner = positions[12]
    facialKeyPoints.mouth_center_top_lip = positions[13]
    facialKeyPoints.mouth_center_bottom_lip = positions[14]

    print(facialKeyPoints)

    return facialKeyPoints

