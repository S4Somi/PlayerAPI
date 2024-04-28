from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from datetime import datetime

class PlayerBase(SQLModel):
    name:str

class PlayerDB(PlayerBase, table=True):
    id: int = Field(default=None, primary_key=True)
    events: list["Event"] = Relationship(back_populates="player")

class EventBase(SQLModel):
    type: str
    detail:str

class Event(EventBase, table=True):
    id: int = Field(default=None, primary_key=True)
    player_id:int = Field(foreign_key="playerdb.id")
    timestamp:datetime = Field(default=datetime.now())
    player: Optional[PlayerDB] = Relationship(back_populates="events")
