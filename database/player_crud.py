from fastapi import HTTPException
from .models import PlayerDB, PlayerBase

# temp dict of players for testing
players = {
    0:{"name":"player1", "player_id":0},
    1:{"name":"player2", "player_id":1},
    2:{"name":"player3", "player_id":2},
}

# get all players in dict, if dict empty return empty, makes sense i think
def find_players():
    if players == {}:
        return []
    return [players[p] for p in players]
   
# find player by id returns name, id, still todo: return events fr
def find_1player(player_id:int):
    if player_id not in players:
        raise HTTPException(status_code=404, detail=f"Player with id {player_id} was not found.")
    return players[player_id]

# add a new player w unique id
def add_player(player_in:PlayerBase):
    new_id=max(players.keys()) + 1
    player = PlayerDB(**player_in.model_dump(), player_id=new_id)
    players[new_id] = player.model_dump()
    return player