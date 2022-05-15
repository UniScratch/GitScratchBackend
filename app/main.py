import uvicorn
from fastapi import FastAPI,Depends
from .config import settings
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world! GitScratch!"}
    
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__=='__main__':
    uvicorn.run(app, host=settings.host_address, port=settings.host_port)
