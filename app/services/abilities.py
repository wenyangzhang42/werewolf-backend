from app.models.roles_enums import Werewolves, Alignment
from app.services import game_info as gi

from app.utils.ability_utils import add_death, remove_death
from app.utils.info_utils import find_alignment


def werewolf(player: int, target: int) -> str:
    gi.night_info["ww_kill"] = target
    add_death(target)
    return f"{target} killed!"


def seer(player: int, target: int) -> str:
    role = gi.game_info.get("roles")[target-1]
    if Werewolves.has_value(role):
        return "Target Identity: BAD!"
    else:
        return "Target Identity: GOOD!"


def witch(player: int, target: int,) -> str:
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


def witch_info() -> str:
    if gi.game_info["witch_save"] is None:
        return f"Player {gi.night_info['ww_kill']} was killed by werewolves tonight!"
    else:
        return "You cannot know who is killed because you have used your cure."


def hunter(player: int, target: int):
    if gi.game_info["hunter_status"]:
        return "You CAN your ability if you are dead!"
    else:
        return "You CANNOT use your ability if you are dead!"


def guard(player: int, target: int):
    if gi.game_info["last_guarded"] == target:
        raise Exception("You cannot guard the same player 2 nights back to back.")
    else:
        gi.game_info["last_guarded"] = target
        gi.night_info["guarded"] = target
        if gi.night_info["witch_save"]:
            add_death(target)
    return f"You have guarded player {target}"


def elder(player: int, target: int):
    gi.night_info["silenced"] = target
    return f"player {target} has been silenced."


def thief_info():
    temp_roles = gi.game_info.get("roles")
    index = len(temp_roles)
    id1 = temp_roles[index-2]
    id2 = temp_roles[index-1]
    return {f"You can type 1 or 2 to choose between 1.{id1} and 2.{id2} !"}


# todo: Thief role unfinished.
def thief(player: int, target: int):
    temp_roles = gi.game_info.get("roles")
    index = len(temp_roles)
    role1 = temp_roles[index - 2]
    role2 = temp_roles[index - 1]
    if target != 1:
        if target != 2:
            raise Exception("Invalid input, please type input 1 or 2.")
        else:
            gi.game_info.get("players")[player-1].role = role2
            gi.game_info.get("players")[player-1].alignment = find_alignment(role2)
            return f"Your new identity is {role2}!"
    else:
        gi.game_info.get("players")[player - 1].role = role1
        gi.game_info.get("players")[player - 1].alignment = find_alignment(role1)
        return f"Your new identity is {role1}!"


def cupid(player: int, target1: int, target2: int):
    gi.game_info["lover_1"] = target1
    gi.game_info["lover_2"] = target2

    al_1 = gi.game_info.get("players")[target1-1].alignment
    al_2 = gi.game_info.get("players")[target2-1].alignment

    if al_1 == Alignment.WEREWOLF:
        if al_2 == Alignment.WEREWOLF:  # bad - bad
            gi.game_info.get("players")[player-1].alignment = Alignment.WEREWOLF
        else:  # bad - good
            gi.game_info.get("players")[target1-1].alignment = Alignment.LOVERS
            gi.game_info.get("players")[target2-1].alignment = Alignment.LOVERS
            gi.game_info.get("players")[player - 1].alignment = Alignment.LOVERS
    else:
        if al_2 == Alignment.WEREWOLF:  # good - bad
            gi.game_info.get("players")[target1 - 1].alignment = Alignment.LOVERS
            gi.game_info.get("players")[target2 - 1].alignment = Alignment.LOVERS
            gi.game_info.get("players")[player - 1].alignment = Alignment.LOVERS
        else:  # good - good
            gi.game_info.get("players")[player - 1].alignment = Alignment.VILLAGER


# todo: Unfinished whild_child logic
def wild_child(player:int, target:int):
    pass


def test(player, target, target2):
    return f"Test succeeded for player {player}, target 1 {target} and target 2 {target2}"
