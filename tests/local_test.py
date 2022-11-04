from app.utils.log_utils import logger
from app.utils.game_utils import invoke
from app.models.roles_enums import Alignment, Gods, Werewolves, Villagers, FenceSitters
import app.services.game_info as gi
import app.services.game as game

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


def set_test_players():
    base_ip = '192.168.0.'
    count = 0
    global roles
    for i in range(1, len(roles)):
        gi.set_player(i, base_ip+str(i))


# (status, msg) = game.setup_game(roles)
# set_test_players()
# gi.debug_print()

s = {"a":123, "b":456}

print(s.get("a"))
s.update({"c": 123})
s.update({"a": 345678})

print(s)


