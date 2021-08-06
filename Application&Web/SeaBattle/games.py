import random
import hashlib

from SeaBattle import game

games = {}


def new_game():
    """
    Содаёт новою игру и Возвращает её id
    """
    while True:
        game_id = hashlib.md5(
            str(random.random()).encode()
        ).hexdigest()
        if game_id not in games:
            games[game_id] = game.GameSession()
            break
    return game_id


def del_game(game_id: str):
    games.pop(game_id, None)


def get_game(game_id:str):
    return games.get(game_id, None)