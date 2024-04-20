from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import *

app = FastAPI()

# CORS, allows requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(players.router)