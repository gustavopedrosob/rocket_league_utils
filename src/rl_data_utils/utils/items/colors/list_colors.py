from re import IGNORECASE
from rl_data_utils.__others import _regex_found_any_in_list
from rl_data_utils.item.color.list_color import ABCListColor
from rl_data_utils.utils.item.color.color import has_color, all_are_colors
from rl_data_utils.utils.items.items.items import get_items_by_condition


def get_items_with_valid_color(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: all_are_colors(item.get_list_color()), items)


def get_items_by_color(color: str, items: list[ABCListColor]):
    return get_items_by_condition(lambda item: has_color(color, item.get_list_color()), items)


def get_items_by_color_regex(color_pattern: str, items: list[ABCListColor], flags=IGNORECASE):
    return get_items_by_condition(
        lambda list_color: _regex_found_any_in_list(color_pattern, list_color.get_list_color(), flags), items)


def get_items_by_color_equal_to(color: str, items: list[ABCListColor]):
    return get_items_by_condition(lambda item: color in item.get_list_color(), items)


def get_items_by_color_contains(color: str, items: list[ABCListColor]):
    return get_items_by_condition(lambda item: any([color in ci for ci in item.get_list_color()]), items)


def get_items_crimson(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_crimson(), items)


def get_items_sky_blue(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_sky_blue(), items)


def get_items_pink(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_pink(), items)


def get_items_orange(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_orange(), items)


def get_items_cobalt(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_cobalt(), items)


def get_items_burnt_sienna(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_burnt_sienna(), items)


def get_items_titanium_white(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_titanium_white(), items)


def get_items_grey(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_grey(), items)


def get_items_saffron(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_saffron(), items)


def get_items_lime(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_lime(), items)


def get_items_forest_green(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_forest_green(), items)


def get_items_black(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_black(), items)


def get_items_purple(items: list[ABCListColor]):
    return get_items_by_condition(lambda item: item.has_purple(), items)