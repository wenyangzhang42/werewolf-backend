from app.services import game_info as gi


def add_death(target: int):
    if target in gi.night_info["dead"]:
        pass
    else:
        gi.night_info["dead"].append(target)


def remove_death(target: int):
    gi.night_info["dead"].remove(target)