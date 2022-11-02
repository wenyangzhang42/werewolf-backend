import random

from app.models.game_infos import game_info_model, night_info_model, every_night_order, first_night_order
from app.models.player import Player
from app.utils.loggers import logger
from app.utils.info_utils import validate_roles, find_alignment

# parameters for the room
nbr_of_players = 0
cur_every_night_order = []
cur_first_night_order = []

# parameters for each game
roles = []
players = []
game_on_going = False
game_start_datetime = None
game_info = game_info_model.copy()
night_info = night_info_model.copy()


def setup(roles_to_set: list):
    (validated, msg) = validate_roles(roles_to_set)
    if not validated:
        raise Exception(msg)

    # If room is not cleared yet. rest() to clear room.
    global nbr_of_players
    if nbr_of_players != 0:
        reset()  # maybe a better way is to reset params for each game here.

    global roles, players, cur_first_night_order, cur_every_night_order, \
        game_info, night_info, game_on_going, game_start_datetime
    roles = roles_to_set.copy()
    random.shuffle(roles)
    for role in first_night_order:
        if role in roles:
            cur_first_night_order.append(role)
    for role in every_night_order:
        if role in roles:
            cur_every_night_order.append(role)
    nbr_of_players = len(roles)
    players = [None]*nbr_of_players
    logger.debug(f"successfully set roles {roles}")
    logger.debug(f"successfully set first night order: {cur_first_night_order}")
    logger.debug(f"successfully set every night order: {cur_every_night_order}")
    logger.debug(f"successfully set empty players list: {players}")


def restart() -> None:
    global roles, players, game_info, night_info, game_on_going, game_start_datetime
    random.shuffle(roles)
    game_on_going = False
    game_start_datetime = None
    try:
        for i in range(nbr_of_players):
            players[i].set_role(roles[i])
            players[i].set_status("alive")
        game_info = game_info_model.copy()
        night_info = night_info_model.copy()
    except Exception as e:
        raise Exception("Unknown Error resetting player roles and status.")
    logger.debug("Game has been reset without changing setups!")


def reset() -> None:
    global roles, players, nbr_of_players, cur_first_night_order, cur_every_night_order,\
        game_info, night_info, game_on_going, game_start_datetime
    nbr_of_players = 0
    game_on_going = False
    game_start_datetime = None
    roles = []
    players = []

    game_info = game_info_model.copy()
    night_info = night_info_model.copy()
    cur_first_night_order = []
    cur_every_night_order = []

    logger.debug("Game successfully reset.")


def set_game_info(field, value):
    global game_info
    game_info[field] = value


def set_night_info(field, value):
    global night_info
    night_info[field] = value


def set_player(seat: int, ip: str):
    global players
    current_seat = find_player_seat(ip)
    if current_seat != -1:
        raise Exception(f"You have already sit on number {current_seat+1}")
    try:
        if players[seat-1] is not None:
            raise Exception(f"Seat {seat} has been taken.")
        else:
            role = roles[seat - 1]
            alignment = find_alignment(role)
            player = Player(ip, seat, role, alignment)
            players[seat-1] = player
            logger.debug("Player " + ip + " seated at seat " + str(seat))
    except Exception as e:
        raise Exception(f"Error set player {ip} at seat {seat}. exception: {e}")


# Helper functions
def find_player_seat(ip: str):
    global players
    for player in players:
        if player is not None and player.ip == ip:
            return player.seat
    return -1


def check_game_is_configured():
    global nbr_of_players
    if nbr_of_players == 0:
        raise Exception("Game is not configured yet!")


def debug_print():  # This will log and print out all current game info for debug uses.
    global roles, players, nbr_of_players, cur_first_night_order, cur_every_night_order, \
        game_info, night_info, game_on_going, game_start_datetime
    print(f"==== DEBUG PRINT START ====")
    print(f"Current roles: {roles}")
    print(f"Current players: {players}")
    print(f"Current game info: {game_info}")
    print(f"Current night info: {night_info}")

    logger.debug(f"==== DEBUG PRINT START ====")
    logger.debug(f"Current roles: {roles}")
    logger.debug(f"Current players: {players}")
    logger.debug(f"Current game info: {game_info}")
    logger.debug(f"Current night info: {night_info}")