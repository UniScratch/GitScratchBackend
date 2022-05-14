import uvicorn
from functools import lru_cache
from fastapi import FastAPI,Depends
from config import settings

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world! GitScratch!"}
    

if __name__=='__main__':
    uvicorn.run(app, host=settings.host_address, port=settings.host_port)