import random
import copy

from app.models.game_infos import room_info_model, game_info_model, night_info_model, public_night_info_model, \
    every_night_order_model, first_night_order_model
from app.models.player import Player
from app.models.roles_enums import FenceSitters, Villagers
from app.utils.log_utils import logger
from app.utils.info_utils import validate_roles, find_alignment

# parameters for the room
room_info = copy.deepcopy(room_info_model)

# parameters for each game
game_info = copy.deepcopy(game_info_model)

# parameters for each night
night_info = copy.deepcopy(night_info_model)
public_night_info = copy.deepcopy(public_night_info_model)


def setup(input_roles: list[str]) -> None:
    (validated, msg) = validate_roles(input_roles)
    if not validated:
        raise Exception(msg)

    global room_info, game_info

    # If room is not cleaned yet. rest() to clean the room.
    if room_info.get("nbr_of_players") != 0:
        reset()

    n_players = len(input_roles)
    roles_to_set = copy.deepcopy(input_roles)

    # special logic for Thief:
    if FenceSitters.THIEF in roles_to_set:
        roles_to_set += [Villagers.VILLAGER.value, Villagers.VILLAGER.value]

    game_info["roles"] = roles_to_set
    random.shuffle(game_info.get("roles"))

    for role in first_night_order_model:
        if role in roles_to_set:
            room_info["first_night_order"].append(role)
    for role in every_night_order_model:
        if role in roles_to_set:
            room_info["first_night_order"].append(role)
            room_info["every_night_order"].append(role)

    room_info.update({"nbr_of_players": n_players})
    game_info.update({"players": [None]*n_players})

    logger.debug(f"successfully set roles {game_info.get('roles')}")
    logger.debug(f"successfully set first night order: {room_info.get('first_night_order')}")
    logger.debug(f"successfully set every night order: {room_info.get('every_night_order')}")
    logger.debug(f"successfully set empty players list: {game_info.get('players')}")


def restart() -> None:
    if not game_is_configured():
        raise Exception("game is not configured!")

    global game_info, night_info, public_night_info

    if None in game_info.get("players"):
        index = game_info.get("players").index(None)
        raise Exception(f"Cannot start game because seat {index+1} is not seated!")

    temp_roles = copy.deepcopy(game_info.get("roles"))
    random.shuffle(temp_roles)

    for i in range(room_info.get("nbr_of_players")):
        game_info["players"][i].set_role(temp_roles[i])
        game_info["players"][i].set_status("alive")

    temp_players = copy.deepcopy(game_info.get('players'))

    game_info = copy.deepcopy(game_info_model)
    night_info = copy.deepcopy(night_info_model)
    public_night_info = copy.deepcopy(public_night_info_model)

    game_info["roles"] = temp_roles
    game_info["players"] = temp_players

    logger.info(f"Game restart, the new roles are now {game_info.get('roles')}")
    logger.debug("Game has been reset without changing setups!")


def reset() -> None:
    global room_info, game_info, night_info, public_night_info

    room_info = copy.deepcopy(room_info_model)
    game_info = copy.deepcopy(game_info_model)
    night_info = copy.deepcopy(night_info_model)
    public_night_info = copy.deepcopy(public_night_info_model)

    logger.debug("Game successfully reset.")


def set_player(seat: int, ip: str) -> None:
    if not game_is_configured():
        raise Exception("game is not configured!")

    global game_info

    current_player = find_player(ip)
    if current_player is not None:
        raise Exception(f"You have already sit on seat {current_player.seat}! ")

    try:
        temp_players = game_info.get("players")
        if temp_players[seat-1] is not None:
            raise Exception(f"Seat {seat} has been taken.")
        else:
            role = game_info.get('roles')[seat - 1]
            alignment = find_alignment(role)
            player = Player(ip, seat, role, alignment)
            temp_players[seat-1] = player
            logger.debug("Player " + ip + " seated at seat " + str(seat))
    except Exception as e:
        raise Exception(f"Unknown error set player {ip} at seat {seat}. exception: {e}")


def get_role(ip: str):
    player = find_player(ip)
    if player is None:
        raise Exception("You have not seated yet!")
    else:
        return player.role


# todo: start game logic
def start_game() -> str:
    if not game_is_configured():
        raise Exception("game is not configured!")

    # todo: add support to Thief
    global game_info

    if None in game_info.get("players"):
        index = game_info.get("players").index(None)
        raise Exception(f"Cannot start game because seat {index+1} is not seated!")

    game_info["round"] += 1

    return move_to_next_stage()


def pre_ability_check(ip: str):
    if not game_is_configured():
        raise Exception("game is not configured!")

    player = find_player(ip)

    if player is None:
        raise Exception("You are not seated.")
    elif player.status != "alive":
        return 403, {"message": f"You are {player.status}. Please wait for others to finish the game."}
    else:
        stage = get_stage()
        if stage != player.role:
            logger.warning(f"player {player.seat} trying to use skill where current stage is {stage}")
            raise Exception("It is not your turn")
        else:
            global room_info
            return {"message": "Please enter your target.",
                    "role": player.role,
                    "seat": player.seat,
                    "count": room_info.get('nbr_of_players')
                    }


def move_to_next_stage() -> str:
    global room_info, game_info, night_info

    stage_index = night_info.get("stage")

    if game_info["round"] == 1:
        if stage_index == len(room_info.get("first_night_order"))-1:
            night_over()
            return "day"
        else:
            night_info["stage"] += 1
            return room_info.get("first_night_order")[stage_index+1]
    else:
        if stage_index == len(room_info.get("every_night_order"))-1:
            night_over()
            return "day"
        else:
            night_info["stage"] += 1
            return room_info.get("first_night_order")[stage_index + 1]


def night_over():
    global game_info, night_info, public_night_info

    night_info.update({"stage": -1})

    temp_players = game_info.get("players")
    for i in public_night_info.get("dead"):
        temp_players[i-1].set_status("dead")


def new_night(exiled: list[int]) -> str:
    if not game_is_configured():
        raise Exception("game is not configured!")

    global game_info, night_info, public_night_info

    if night_info.get("stage") != -1:
        raise Exception("Cannot move on to next night. now is not daytime!")

    for i in exiled:
        game_info.get("players")[i-1].set_status("dead")

    # todo: maybe win_check

    game_info["round"] += 1
    night_info = copy.deepcopy(night_info_model)
    public_night_info = copy.deepcopy(public_night_info_model)

    return move_to_next_stage()


def get_night_info():
    if not game_is_configured():
        raise Exception("game is not configured!")

    stage = get_stage()
    if stage == "day":
        global public_night_info
        return public_night_info
    else:
        raise Exception("You can only check last night info during day time.")


# Helper functions
def find_player(ip: str):
    global game_info
    for player in game_info.get("players"):
        if player is not None and player.ip == ip:
            return player
    return None


def get_stage() -> str:
    global room_info, game_info, night_info
    if game_info.get("round") == 0:
        raise Exception("Game not set or game not started!")
    else:
        stage_index = night_info.get("stage")
        if stage_index == -1:
            return "day"
        elif game_info.get("round") == 1:
            return room_info.get("first_night_order")[stage_index]
        else:
            return room_info.get("every_night_order")[stage_index]


def game_is_configured() -> bool:
    global room_info
    if room_info.get("nbr_of_players") == 0:
        return False
    return True


def debug_print():  # This will log and print out all current game info for debug uses.
    global room_info, game_info, night_info

    print(f"==== DEBUG PRINT START ====")
    print(f"Current room settings: {room_info}")
    print(f"Current game info: {game_info}")
    print(f"Current night info: {night_info}")

    logger.debug(f"==== DEBUG PRINT START ====")
    logger.debug(f"Current room settings: {room_info}")
    logger.debug(f"Current game info: {game_info}")
    logger.debug(f"Current night info: {night_info}")
