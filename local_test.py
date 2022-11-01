from app.utils.loggers import logger
from app.models.roles_enums import Gods, Werewolves, Villagers
import app.services.game_info as gi
from app.services.game import game_setup

logger.debug("Debug test started")

roles = [
    Villagers.VILLAGER,
    Villagers.VILLAGER,
    Villagers.VILLAGER,

    Gods.SEER,
    Gods.WITCH,
    Gods.GUARD,

    Werewolves.WEREWORLF,
    Werewolves.WEREWORLF,
    Werewolves.WEREWORLF
]


(status, msg) = game_setup(roles)

