from app.services import game_info as gi


def add_death(target: int):
    if target in gi.public_night_info["dead"]:
        pass
    else:
        gi.public_night_info["dead"].append(target)


def remove_death(target: int):
    gi.public_night_info["dead"].remove(target)
