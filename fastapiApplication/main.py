from fastapi import FastAPI, File, UploadFile 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import os 
import pandas as pd 


app=FastAPI()

UPLOAD_FOLDER="ressources"

