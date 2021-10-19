from rocket_league_utils.__others import _regex_found
from rocket_league_utils.colors.constants import *


def is_black(color: str) -> bool:
    return "black" in color.lower()


def is_titanium_white(color: str) -> bool:
    return _regex_found(r"white|tw", color)


def is_grey(color: str) -> bool:
    return "grey" in color.lower()


def is_crimson(color: str) -> bool:
    return _regex_found(r"crimson|carmesim", color)


def is_pink(color: str) -> bool:
    return "pink" in color.lower()


def is_cobalt(color: str) -> bool:
    return _regex_found(r"cobalt", color)


def is_sky_blue(color: str) -> bool:
    return _regex_found(r"sky[_\- ]?blue|sb", color)


def is_burnt_sienna(color: str) -> bool:
    return _regex_found(r"burnt[_\- ]?sienna|bs", color)


def is_saffron(color: str) -> bool:
    return _regex_found(r"saffron|yellow", color)


def is_lime(color: str) -> bool:
    return "lime" in color.lower()


def is_forest_green(color: str) -> bool:
    return _regex_found(r"fg|green", color)


def is_orange(color: str) -> bool:
    return "orange" in color.lower()


def is_purple(color: str) -> bool:
    return "purple" in color.lower()


def is_default(color: str) -> bool:
    return _regex_found(r"default|regular|none", color)
