from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.item.type.regexs import *


def is_antenna(type_: str) -> bool:
    return _regex_found(IS_ANTENNA, type_)


def is_avatar_border(type_: str) -> bool:
    return _regex_found(IS_AVATAR_BORDER, type_)


def is_banner(type_: str) -> bool:
    return _regex_found(IS_BANNER, type_)


def is_boost(type_: str) -> bool:
    return _regex_found(IS_BOOST, type_)


def is_car(type_: str) -> bool:
    return _regex_found(IS_CAR, type_)


def is_decal(type_: str) -> bool:
    return _regex_found(IS_DECAL, type_)


def is_engine_audio(type_: str) -> bool:
    return _regex_found(IS_ENGINE_AUDIO, type_)


def is_gift_pack(type_: str) -> bool:
    return _regex_found(IS_GIFT_PACK, type_)


def is_goal_explosion(type_: str) -> bool:
    return _regex_found(IS_GOAL_EXPLOSION, type_)


def is_paint_finish(type_: str) -> bool:
    return _regex_found(IS_PAINT_FINISH, type_)


def is_player_anthem(type_: str) -> bool:
    return _regex_found(IS_PLAYER_ANTHEM, type_)


def is_topper(type_: str) -> bool:
    return _regex_found(IS_TOPPER, type_)


def is_trail(type_: str) -> bool:
    return _regex_found(IS_TRAIL, type_)


def is_wheel(type_: str) -> bool:
    return _regex_found(IS_WHEEL, type_)


IS_FUNCTIONS = [is_antenna, is_avatar_border, is_banner, is_boost, is_car, is_decal, is_engine_audio, is_gift_pack,
                is_goal_explosion, is_paint_finish, is_player_anthem, is_topper, is_trail, is_wheel]
