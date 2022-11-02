from enum import Enum


class Alignment(str, Enum):
    GOD = "god"
    VILLAGER = "villager"
    WEREWOLF = "werewolf"
    LOVERS = "lovers"
    IRRELEVANT = "irrelevant"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class Gods(str, Enum):
    SEER = "seer"
    WITCH = "witch"
    HUNTER = "hunter"
    IDIOT = "idiot"
    GUARD = "guard"
    KNIGHT = "knight"
    ELDER = "elder"
    LITTLEGIRL = "little girl"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class FenceSitters(str, Enum):
    CUPID = "cupid"
    THIEF = "thief"
    WILDCHILD = "wild child"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class Werewolves(str, Enum):
    WEREWORLF = "werewolf"
    WHITEWOLF = "white wolf"
    WOLFKING = "wolf king"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class Villagers(str, Enum):
    VILLAGER = "villager"
    ANGEL = "angel"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_





