from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import *
from typing import Optional

router = APIRouter(prefix="/events")

# get all events in db
@router.get("/", response_model=list[models.Event], status_code=200)
def get_events(*, session:Session=Depends(database.get_session), type:Optional[str]=None):
    events= events_crud.find_events(session, type)
    return events
