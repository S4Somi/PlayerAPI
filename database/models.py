from pydantic import BaseModel


class PlayerBase(BaseModel):
    name:str

class PlayerDB(PlayerBase):
    player_id:int
    
class PlayersEvents(PlayerDB):
    events:list[str] = []


# event model inherits player_id from PlayerDB ?
class Event(PlayerDB):
    event_id:int
    type:str
    detail:str
    timestamp:str # from datetime import datetime / datetime.now() ?