from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import helps
import requests
from flask import request
from pydantic import BaseModel

app = FastAPI()
origins = [
    'https://kaherclient.netlify.app/',
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials= True,
    allow_headers = ["*"]
)

class City(BaseModel):
    name : str

@app.get('/')
def test():
    return ('Hello there')
@app.post("/data/")
async def getCity(city:City):
    cityName = str(city.name)
    print(cityName)
    await helps.myData(cityName)
    return "Done"
    
    



if __name__== '__main__':
    uvicorn.run(app,port=5000,host="127.0.0.1")