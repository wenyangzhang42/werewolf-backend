from app.models.roles_enums import Werewolves
from app.services import game_info as gi

from app.utils.ability_utils import add_death, remove_death


def werewolf(target: int) -> str:
    gi.night_info["ww_kill"] = target
    add_death(target)
    return f"{target} killed!"


def seer(target: int) -> str:
    role = gi.roles[target-1]
    if Werewolves.has_value(role):
        return "Target Identity: BAD!"
    else:
        return "Target Identity: GOOD!"


def witch(target: int, player: int) -> str:
    # cure used, poisoning.
    if gi.game_info["witch_save"] is not None:
        if gi.game_info["witch_kill"] is not None:  # poison also used, skipping
            return "You have used both poison and cure potions. Game moves on."
        else:  # poisoning target
            gi.game_info["witch_kill"] = target
            gi.night_info["witch_kill"] = target
            add_death(target)
            return f"You have poisoned player {target}."

    # cure not used.
    else:
        # curing target
        if gi.night_info["ww_kill"] == target:
            if player == target:  # self-cure
                if gi.game_info["round"] == 1:
                    gi.night_info["ww_kill"] = None
                    gi.night_info["witch_save"] = target
                    gi.night_info["dead"].remove(target)
                    gi.game_info["witch_save"] = target
                    remove_death(target)
                    return f"You have saved player {target} with your cure."
                else:
                    raise Exception("you cannot save yourself unless tonight is the first night.")
            else:  # cure others
                gi.night_info["ww_kill"] = None
                gi.night_info["witch_save"] = target
                gi.game_info["witch_save"] = target
                remove_death(target)
                return f"You have saved player {target} with your cure."
        # poisoning target
        else:
            gi.game_info["witch_kill"] = target
            gi.night_info["witch_kill"] = target
            add_death(target)
            return f"You have poisoned player {target}."


def witch_info():
    if gi.game_info["witch_save"] is None:
        return f"Player {gi.night_info['ww_kill']} was killed by werewolves tonight!"
    else:
        return "You cannot know who is killed because you have used your cure."
