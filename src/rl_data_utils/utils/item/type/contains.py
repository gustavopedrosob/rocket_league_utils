from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.item.type.regexs import *


def contains_antenna(type_: str) -> bool:
    return _regex_found(CONTAINS_ANTENNA, type_)


def contains_avatar_border(type_: str) -> bool:
    return _regex_found(CONTAINS_AVATAR_BORDER, type_)


def contains_banner(type_: str) -> bool:
    return _regex_found(CONTAINS_BANNER, type_)


def contains_blueprint(type_: str) -> bool:
    return _regex_found(CONTAINS_BLUEPRINT, type_)


def contains_boost(type_: str) -> bool:
    return _regex_found(CONTAINS_BOOST, type_)


def contains_car(type_: str) -> bool:
    return _regex_found(CONTAINS_CAR, type_)


def contains_decal(type_: str) -> bool:
    return _regex_found(CONTAINS_DECAL, type_)


def contains_engine_audio(type_: str) -> bool:
    return _regex_found(CONTAINS_ENGINE_AUDIO, type_)


def contains_gift_pack(type_: str) -> bool:
    return _regex_found(CONTAINS_GIFT_PACK, type_)


def contains_goal_explosion(type_: str) -> bool:
    return _regex_found(CONTAINS_GOAL_EXPLOSION, type_)


def contains_paint_finish(type_: str) -> bool:
    return _regex_found(CONTAINS_PAINT_FINISH, type_)


def contains_player_anthem(type_: str) -> bool:
    return _regex_found(CONTAINS_PLAYER_ANTHEM, type_)


def contains_player_title(type_: str) -> bool:
    return _regex_found(CONTAINS_PLAYER_TITLE, type_)


def contains_topper(type_: str) -> bool:
    return _regex_found(CONTAINS_TOPPER, type_)


def contains_trail(type_: str) -> bool:
    return _regex_found(CONTAINS_TRAIL, type_)


def contains_wheel(type_: str) -> bool:
    return _regex_found(CONTAINS_WHEEL, type_)


CONTAINS_FUNCTIONS = [contains_antenna, contains_avatar_border, contains_banner, contains_blueprint, contains_boost,
                      contains_car, contains_decal, contains_engine_audio, contains_gift_pack, contains_goal_explosion,
                      contains_paint_finish, contains_player_anthem, contains_player_title, contains_topper,
                      contains_trail, contains_wheel]
