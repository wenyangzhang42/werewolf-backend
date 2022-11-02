from app.utils.loggers import logger
from app.models.roles_enums import Alignment, Gods, Werewolves, Villagers, FenceSitters
import app.services.game_info as gi
from app.services.game import setup_game

logger.debug("Debug test started")

roles = [
    Villagers.VILLAGER,
    Villagers.VILLAGER,
    Villagers.VILLAGER,

    Gods.SEER,
    Gods.WITCH,
    Gods.HUNTER,

    Werewolves.WEREWORLF,
    Werewolves.WEREWORLF,
    Werewolves.WEREWORLF
]


# (status, msg) = setup_game(roles)