from app.utils.loggers import logger
import app.services.game_info as gi


def game_setup(roles: list):
    try:
        gi.set_roles(roles)
    except Exception as e:
        logger.error("Error setting roles for the game!", str(e))
        logger.error(roles)
        return 500, "Error setting roles :" + str(e)

    gi.set_nbr_of_players(len(roles))
    return 200, "Set roles: " + str(roles)
