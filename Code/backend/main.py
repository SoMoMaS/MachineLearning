from ast import List
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

import tensorflow as tf

class Picture(BaseModel):
    pixels: list = []


# Load models
ml_model_10_epochs = tf.keras.models.load_model('./Models/10/facial_keypoint_model_10_epochs.keras')
ml_model_50_epochs = tf.keras.models.load_model('./Models/50/facial_keypoint_model_50_epochs.keras')
ml_model_100_epochs = tf.keras.models.load_model('./Models/100/facial_keypoint_model_100_epochs.keras')



app = FastAPI()

@app.get("/facialkeypoints/epochs_10")
async def get_facial_keypoints(picture: Picture):
    print(picture.pixels)
    return {"Epochs": "10"}

@app.get("/facialkeypoints/epochs_50")
async def get_facial_keypoints(picture: Picture):
    print(picture.pixels)
    return {"Epochs": "50"}

@app.get("/facialkeypoints/epochs_100")
async def get_facial_keypoints(picture: Picture):
    print(picture.pixels)
    return {"Epochs": "100"}

