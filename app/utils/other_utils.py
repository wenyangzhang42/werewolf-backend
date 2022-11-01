from app.models.roles_enums import Alignment


def find_alignment(role: str) -> str:
    if role == "villager":
        return Alignment.VILLAGER
    if role == "werewolf" or role == "white wolf" or role == "wolf king":
        return Alignment.WEREWOLF
    else:
        return Alignment.GOD
