from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import helps

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

@app.get('/')
def test():
    return ('Hello there')
@app.post('/{city}')
async def getCity(city:str):
    city = city
    print('City selected: '+city)
    res = await helps.myData(city)
    return res
if __name__== '__main__':
    uvicorn.run(app,port=5000,host="127.0.0.1")