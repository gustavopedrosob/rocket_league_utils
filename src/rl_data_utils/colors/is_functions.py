from rl_data_utils.__others import _regex_found
from rl_data_utils.colors.regexs import *


def is_black(color: str) -> bool:
    return _regex_found(IS_BLACK, color)


def is_burnt_sienna(color: str) -> bool:
    return _regex_found(IS_BURNT_SIENNA, color)


def is_cobalt(color: str) -> bool:
    return _regex_found(IS_COBALT, color)


def is_crimson(color: str) -> bool:
    return _regex_found(IS_CRIMSON, color)


def is_default(color: str) -> bool:
    return _regex_found(IS_DEFAULT, color)


def is_forest_green(color: str) -> bool:
    return _regex_found(IS_FOREST_GREEN, color)


def is_grey(color: str) -> bool:
    return _regex_found(IS_GREY, color)


def is_lime(color: str) -> bool:
    return _regex_found(IS_LIME, color)


def is_orange(color: str) -> bool:
    return _regex_found(IS_ORANGE, color)


def is_pink(color: str) -> bool:
    return _regex_found(IS_PINK, color)


def is_purple(color: str) -> bool:
    return _regex_found(IS_PURPLE, color)


def is_saffron(color: str) -> bool:
    return _regex_found(IS_SAFFRON, color)


def is_sky_blue(color: str) -> bool:
    return _regex_found(IS_SKY_BLUE, color)


def is_titanium_white(color: str) -> bool:
    return _regex_found(IS_TITANIUM_WHITE, color)


IS_FUNCTIONS = [is_black, is_burnt_sienna, is_cobalt, is_crimson, is_default, is_forest_green, is_grey, is_lime,
                is_orange, is_pink, is_purple, is_saffron, is_sky_blue, is_titanium_white]
