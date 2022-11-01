from enum import Enum


class Alignment(str, Enum):
    GOD = "god"
    VILLAGER = "villager"
    WEREWOLF = "werewolf"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class Gods(str, Enum):
    SEER = "seer"
    WITCH = "witch"
    HUNTER = "hunter"
    IDIOT = "idiot"
    GUARD = "guard"
    CUPID = "cupid"


class Werewolves(str, Enum):
    WEREWORLF = "werewolf"
    WHITEWOLF = "white wolf"
    WOLFKING = "wolf king"


class Villagers(str, Enum):
    VILLAGER = "villager"





