from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from database import *
from database.models import PlayerBase, EventBase, PlayerDB, Event
from typing import Optional

router = APIRouter(prefix="/players")

# returns a list of all players
@router.get("/", response_model=list[PlayerDB], status_code=200)
def get_players(*, session:Session=Depends(database.get_session)):
    player= player_crud.find_players(session)
    return player

# rn returns only name and id but events also have to be returned
@router.get("/{id}", status_code=200)
def get_1player(*, session:Session=Depends(database.get_session), id:int):
    player = player_crud.find_1player(session, id)
    if not player:
        raise HTTPException(status_code=404, detail=f"Player with id {id} not found.")
    return player


# creates a new player
@router.post("/", status_code=201)
def create_player(*, session:Session=Depends(database.get_session), player_in:PlayerBase):
    if not isinstance(player_in.name, str):
        raise HTTPException(status_code=422, detail=f"Name must be a str.")
    player = player_crud.add_player(session, player_in)
    return player


# creates a new event for a chosen player by id
@router.post("/{id}/events", status_code=201)
def create_event(*, session:Session=Depends(database.get_session), event_in:EventBase, id:int):
    event = events_crud.add_event(session, event_in, id=id)
    return event


#returns a players events by player_id
@router.get("/{id}/events", response_model=list[Event], status_code=200)
def get_player_events(*, session:Session=Depends(database.get_session), id:int, type:Optional[str]=None):
    return events_crud.find_player_events(session, id, type)
