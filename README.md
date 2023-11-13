# MachineLearning
This repository contains a facial recognition project for the machine learning subject of the MSE at FHTW.

## TODOs

### Backend
- [X] Augmentation not right
- [X] Plot will be saved as 389x389 instead of 480x480
- [X] Pixels are not sent back in a correct form
- [X] Clean up

### Frontend
- [ ] Improve design
- [X] Display new image from the backend


## Start project

### Backend
The server was written in the **FastAPI** framework with python. In this section you'll find information how to start the server.
From the root folder change the directory to the folder of backend with the following command: 
```console
cd ./Code/backend
```

Start the server with **uvicorn** like following: 
```console
uvicorn main:app --reload
```

As default the server will be running on localhost port 8000. To access a documentation of the avaliable endpoints click [here](http://localhost:8000/docs).


### Frontend
