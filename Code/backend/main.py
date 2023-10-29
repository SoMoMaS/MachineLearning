from ast import List
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from facial_keypoint import FacialKeyPoints, Position

import tensorflow as tf
import numpy as np

class Picture(BaseModel):
    pixels: list = []


# Load models
ml_model_10_epochs = tf.keras.models.load_model('./Models/10/facial_keypoint_model_10_epochs.keras')
ml_model_50_epochs = tf.keras.models.load_model('./Models/50/facial_keypoint_model_50_epochs.keras')
ml_model_100_epochs = tf.keras.models.load_model('./Models/100/facial_keypoint_model_100_epochs.keras')


app = FastAPI()

@app.get("/facialkeypoints/epochs_10")
async def get_facial_keypoints(picture: Picture) -> FacialKeyPoints:
    formatedPixels = preparePixelData(picture.pixels)
    predicted_points = ml_model_10_epochs.predict(formatedPixels)[0]
    facialKeypoints = convertToFacialKeypoints(predicted_points)
    return facialKeypoints

@app.get("/facialkeypoints/epochs_50")
async def get_facial_keypoints(picture: Picture):
    formatedPixels = preparePixelData(picture.pixels)
    predicted_points = ml_model_50_epochs.predict(formatedPixels)[0]
    facialKeypoints = convertToFacialKeypoints(predicted_points)
    return facialKeypoints

@app.get("/facialkeypoints/epochs_100")
async def get_facial_keypoints(picture: Picture):
    formatedPixels = preparePixelData(picture.pixels)
    predicted_points = ml_model_100_epochs.predict(formatedPixels)[0]
    facialKeypoints = convertToFacialKeypoints(predicted_points)
    return facialKeypoints



def preparePixelData(pixels):
    data = []
    test_imgs_arr = np.array(pixels, dtype='float')
    test_imgs_arr = np.reshape(test_imgs_arr, (1, 96, 96, 1))
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

