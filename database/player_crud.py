from .models import PlayerDB, PlayerBase, Event
from sqlmodel import Session, select

# finds all players in the database
def find_players(session:Session):
    return session.exec(select(PlayerDB)).all()


# finds player by id, returns name, id, events
def find_1player(session:Session, id:int):
    statement = select(PlayerDB).join(Event, isouter=True).where(PlayerDB.id==id)
    results = session.exec(statement)
    for player in results:
        return {"player":player, "events":player.events}


# adds a new player to the database
def add_player(session:Session, player_in:PlayerBase):
    players_db = PlayerDB.model_validate(player_in)
    session.add(players_db)
    session.commit()
    session.refresh(players_db)
    return players_db