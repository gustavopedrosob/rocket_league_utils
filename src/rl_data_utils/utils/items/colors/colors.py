from re import IGNORECASE
from rl_data_utils.__others import _regex_found
from rl_data_utils.item.color.color import ABCColor
from rl_data_utils.utils.item.color.color import validate_color
from rl_data_utils.utils.items.items.items import get_items_by_condition
from rl_data_utils.item.color.color import compare_colors


def get_colors(items: list[ABCColor]):
    return {item.get_color() for item in items}


def get_items_by_color(color: str, items: list[ABCColor]):
    validate_color(color)
    return get_items_by_condition(lambda item: compare_colors(item.get_color(), color), items)


def get_items_by_color_regex(color_pattern: str, items: list[ABCColor], flags=IGNORECASE):
    return get_items_by_condition(lambda item: _regex_found(color_pattern, item.get_color(), flags), items)


def get_items_by_color_equal_to(color: str, items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.get_color() == color, items)


def get_items_by_color_contains(color: str, items: list[ABCColor]):
    return get_items_by_condition(lambda item: color in item.get_color(), items)


def get_items_crimson(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_crimson(), items)


def get_items_sky_blue(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_sky_blue(), items)


def get_items_pink(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_pink(), items)


def get_items_orange(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_orange(), items)


def get_items_cobalt(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_cobalt(), items)


def get_items_burnt_sienna(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_burnt_sienna(), items)


def get_items_titanium_white(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_titanium_white(), items)


def get_items_grey(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_grey(), items)


def get_items_saffron(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_saffron(), items)


def get_items_lime(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_lime(), items)


def get_items_forest_green(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_forest_green(), items)


def get_items_black(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_black(), items)


def get_items_purple(items: list[ABCColor]):
    return get_items_by_condition(lambda item: item.is_purple(), items)
