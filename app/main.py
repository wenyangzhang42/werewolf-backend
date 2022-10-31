from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from app.api_router import router as api_router

origins = ["*"] # This will eventually be changed to only the origins you will use once it's deployed, to secure the app a bit more.

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# @app.get('/')
# def test():
#     return {"Ping": "Pong"}

app.include_router(api_router)

handler = Mangum(app)
