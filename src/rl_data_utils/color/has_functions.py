from rl_data_utils.color.is_functions import *


def has_black(colors: list[str]) -> bool:
    return any([is_black(color) for color in colors])


def has_burnt_sienna(colors: list[str]) -> bool:
    return any([is_burnt_sienna(color) for color in colors])


def has_cobalt(colors: list[str]) -> bool:
    return any([is_cobalt(color) for color in colors])


def has_crimson(colors: list[str]) -> bool:
    return any([is_crimson(color) for color in colors])


def has_default(colors: list[str]) -> bool:
    return any([is_default(color) for color in colors])


def has_forest_green(colors: list[str]) -> bool:
    return any([is_forest_green(color) for color in colors])


def has_grey(colors: list[str]) -> bool:
    return any([is_grey(color) for color in colors])


def has_lime(colors: list[str]) -> bool:
    return any([is_lime(color) for color in colors])


def has_orange(colors: list[str]) -> bool:
    return any([is_orange(color) for color in colors])


def has_pink(colors: list[str]) -> bool:
    return any([is_pink(color) for color in colors])


def has_purple(colors: list[str]) -> bool:
    return any([is_purple(color) for color in colors])


def has_saffron(colors: list[str]) -> bool:
    return any([is_saffron(color) for color in colors])


def has_sky_blue(colors: list[str]) -> bool:
    return any([is_sky_blue(color) for color in colors])


def has_titanium_white(colors: list[str]) -> bool:
    return any([is_titanium_white(color) for color in colors])
