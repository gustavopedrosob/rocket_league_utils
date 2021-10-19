from rocket_league_utils.types.isandcompare import TypeIsAndCompare
from rocket_league_utils.types.is_functions import *
from rocket_league_utils.types.constants import *


def is_type(string: str) -> bool:
    return TypeIsAndCompare.is_(string)


def compare_types(type_1: str, type_2: str) -> bool:
    return TypeIsAndCompare.compare_(type_1, type_2)


def get_respective_type(type_: str) -> str:
    if is_engine_audio(type_):
        return ENGINE_AUDIO
    elif is_banner(type_):
        return PLAYER_BANNERS
    elif is_car(type_):
        return BODIES
    elif is_topper(type_):
        return TOPPERS
    elif is_goal_explosion(type_):
        return GOAL_EXPLOSIONS
    elif is_wheel(type_):
        return WHEELS
    elif is_player_anthem(type_):
        return PLAYER_ANTHEMS
    elif is_decal(type_):
        return DECALS
    elif is_paint_finish(type_):
        return PAINT_FINISHES
    elif is_decal(type_):
        return DECALS
    elif is_avatar_border(type_):
        return AVATAR_BORDERS
    elif is_antenna(type_):
        return ANTENNAS
    elif is_boost(type_):
        return ROCKET_BOOST
    elif is_trail(type_):
        return TRAILS


class Type:
    def __init__(self, type_: str):
        self.type = type_

    def is_car(self) -> bool:
        return is_car(self.type)

    def is_decal(self) -> bool:
        return is_decal(self.type)

    def is_paint_finish(self) -> bool:
        return is_paint_finish(self.type)

    def is_wheel(self) -> bool:
        return is_wheel(self.type)

    def is_boost(self) -> bool:
        return is_boost(self.type)

    def is_topper(self) -> bool:
        return is_topper(self.type)

    def is_antenna(self) -> bool:
        return is_antenna(self.type)

    def is_goal_explosion(self) -> bool:
        return is_goal_explosion(self.type)

    def is_trail(self) -> bool:
        return is_trail(self.type)

    def is_engine_audio(self) -> bool:
        return is_engine_audio(self.type)

    def is_banner(self) -> bool:
        return is_banner(self.type)

    def is_avatar_border(self) -> bool:
        return is_avatar_border(self.type)

    def is_gift_pack(self) -> bool:
        return is_gift_pack(self.type)

    def is_player_anthem(self):
        return is_player_anthem(self.type)

    def compare_types(self, type_: str) -> bool:
        return compare_types(self.type, type_)

    def get_respective_type(self) -> str:
        return get_respective_type(self.type)
