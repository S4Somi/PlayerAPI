from fastapi import HTTPException
from .models import Event, PlayerDB, EventBase
from sqlmodel import Session, select
from typing import Optional

known_event_types = {
    "level_started", 
    "level_solved"
}

# finds all events in db, can optionally filter by type
def find_events(session:Session, type:Optional[str]=None):
    if type:
        events = session.exec(select(Event).where(Event.type == type)).all()
        if not events:
            raise HTTPException(status_code=400, detail=f"Unknown event type.")
        return events
    return session.exec(select(Event)).all()

# adds new event, returns error if player by id is not found or if the event type is not valid
def add_event(session:Session, event_in:EventBase, id:int):
    player = session.get(PlayerDB, id)
    if not player:
        raise HTTPException(status_code=404, detail=f"Player with id {id} not found.")
    if event_in.type not in known_event_types:
        raise HTTPException(status_code=400, detail=f"Event type is not valid")
    events_db = Event(**event_in.model_dump(), player_id=id)
    session.add(events_db)
    session.commit()
    session.refresh(events_db)
    return events_db

#finds player's events by player id, can optionally filter by type
# returns error if player by id is not found, input type is not valid or if player does not have filtered event type
def find_player_events(session:Session, id:int, type:Optional[str]=None):
    player = session.get(PlayerDB, id)
    if not player:
        raise HTTPException(status_code=404, detail=f"Unknown player.")
    if type:
        if type not in known_event_types:
            raise HTTPException(status_code=400, detail=f"Event type is not valid")
        events = session.exec(select(Event).where(Event.player_id==id, Event.type==type)).all()
        if not events:
            raise HTTPException(status_code=400, detail=f"Player does not have this event type.")
        return events
    events = session.exec(select(Event).where(Event.player_id==id)).all()        
    return events
