from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import *
from database import *

# defining what happens during lifespan of api
# creating the database
@asynccontextmanager
async def lifespan(app:FastAPI):
    database.createDB()
    yield

app = FastAPI(lifespan=lifespan)


# CORS, allows requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(players.router)
app.include_router(events.router)