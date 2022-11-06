from app.utils.log_utils import logger
from app.utils.game_utils import invoke
import app.services.game_info as gi


def setup_game(roles: list):
    try:
        while '' in roles:
            roles.remove('')

        gi.setup(roles)
    except Exception as e:
        logger.error("Error setting up the game!", e)
        return 500, {"message": "Cannot set roles for the game!", "error": str(e)}
    logger.info(f"game set up with roles: {roles}")
    return 200, {"message": f"game setup with roles: {str(roles)}", "count": len(roles)}


def restart_game():
    try:
        gi.restart()
    except Exception as e:
        logger.error(f"Error restarting game, Error: {e}")
        return 500, {"message": "Error restarting game!", "error": str(e)}
    logger.info(f"Game reset without changing configuration.")
    return 200, {"message": "Game successfully reset!"}


def reset_game():
    try:
        gi.reset()
    except Exception as e:
        logger.error(f"Error Clear game settings, Error: {e}")
        return 500, {"message": "Error Clear game settings,", "error": str(e)}

    logger.info(f"Successfully cleared game settings.")
    return 200, {"message": "Successfully cleared game settings."}


def set_player(seat: int, ip: str):
    try:
        gi.set_player(seat, ip)
    except Exception as e:
        logger.error(f"Error setting player, Error: {e}")
        return 500, {"message": "Error setting player!", "error": str(e)}

    logger.info(f"player {ip} sit on seat {seat}")
    return 200, {"message": f"You sit on seat {seat}!"}


def get_role(ip: str):
    try:
        temp_role = gi.get_role(ip)
    except Exception as e:
        return 404, {"message": "Error getting role!", "error": str(e)}

    return 200, {"message": f"Your role is {temp_role}"}

def pre_check(ip: str):
    try:
        check_result = gi.pre_ability_check(ip)
    except Exception as e:
        print(e)
        return 404, {"message": "Error using ability!", "error": str(e)}

    return 200, check_result


def use_ability(player_role: str, player_seat: str, targets: str):
    # todo: maybe need to move this logic to game_info.py or put it in try block
    try:
        targets = targets.split(',')
        while '' in targets:
            targets.remove('')
        targets = map(lambda x: int(x), targets)
        targets = list(targets)

        eval_result = invoke(player_role, player_seat, targets)

        next_stage = gi.move_to_next_stage()
        return 200, {"message": eval_result, "stage": next_stage}

    except Exception as e:
        return 500, {"message": f"Error suing ability!", "error": str(e)}


def start_game():
    try:
        next_stage = gi.start_game()
    except Exception as e:
        return 500, {"message": "Error starting game!", "error": str(e)}

    return 200, {"message": "Game started!", "next_stage": next_stage}


# Game Process Handlers
def get_night_info():
    try:
        night_info = gi.get_night_info()
    except Exception as e:
        return 500, {"message": f"Error getting last night info!", "error": str(e)}

    logger.info(f"last night's info is {night_info.get('dead')}")
    return 200, {"message": "last night info: ", "info": night_info}


def next_night(exiled: str):
    try:
        exiled = exiled.split(',')
        while '' in exiled:
            exiled.remove('')
        exiled = map(lambda x: int(x), exiled)

        next_stage = gi.new_night(exiled)
    except Exception as e:
        return 500, {"message": "Error moving to next night!", "error": str(e)}

    return 200, {"message": "Next night began!", "next_stage": next_stage}

