from fastapi import APIRouter, HTTPException
from database import *
from database.models import PlayerBase

router = APIRouter(prefix="/players")

@router.get("/", response_model=list[models.PlayerDB], status_code=200)
def get_players():
    return player_crud.find_players()

@router.get("/{id}", response_model=models.PlayersEvents, status_code=200)
def get_1player(id:int):
    return player_crud.find_1player(id)

@router.post("/", status_code=201)
def create_player(player_in:PlayerBase):
    if not isinstance(player_in.name, str):
        raise HTTPException(status_code=422, detail=f"Name must be a str.")
    return player_crud.add_player(player_in)
    