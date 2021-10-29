from rl_data_utils.__others import _regex_found
from rl_data_utils.color.regexs import *


def contains_black(color: str) -> bool:
    return _regex_found(CONTAINS_BLACK, color)


def contains_burnt_sienna(color: str) -> bool:
    return _regex_found(CONTAINS_BURNT_SIENNA, color)


def contains_cobalt(color: str) -> bool:
    return _regex_found(CONTAINS_COBALT, color)


def contains_crimson(color: str) -> bool:
    return _regex_found(CONTAINS_CRIMSON, color)


def contains_default(color: str) -> bool:
    return _regex_found(CONTAINS_DEFAULT, color)


def contains_forest_green(color: str) -> bool:
    return _regex_found(CONTAINS_FOREST_GREEN, color)


def contains_grey(color: str) -> bool:
    return _regex_found(CONTAINS_GREY, color)


def contains_lime(color: str) -> bool:
    return _regex_found(CONTAINS_LIME, color)


def contains_orange(color: str) -> bool:
    return _regex_found(CONTAINS_ORANGE, color)


def contains_pink(color: str) -> bool:
    return _regex_found(CONTAINS_PINK, color)


def contains_purple(color: str) -> bool:
    return _regex_found(CONTAINS_PURPLE, color)


def contains_saffron(color: str) -> bool:
    return _regex_found(CONTAINS_SAFFRON, color)


def contains_sky_blue(color: str) -> bool:
    return _regex_found(CONTAINS_SKY_BLUE, color)


def contains_titanium_white(color: str) -> bool:
    return _regex_found(CONTAINS_TITANIUM_WHITE, color)


CONTAINS_FUNCTIONS = [contains_black, contains_burnt_sienna, contains_cobalt, contains_crimson, contains_default,
                      contains_forest_green, contains_grey, contains_lime,
                      contains_orange, contains_pink, contains_purple, contains_saffron, contains_sky_blue,
                      contains_titanium_white]
