from rl_data_utils.__others import AttributesFunctions
from rl_data_utils.exceptions import ColorNotExists, InvalidColorsList
from rl_data_utils.utils.item.color.constants import COLORS
from rl_data_utils.utils.item.color.contains import CONTAINS_FUNCTIONS
from rl_data_utils.utils.item.color.regexs import CONTAINS_REGEXS
from rl_data_utils.utils.item.color.is_functions import IS_FUNCTIONS, is_crimson, is_sky_blue, is_pink, is_orange, \
    is_cobalt, is_titanium_white, is_burnt_sienna, is_grey, is_saffron, is_lime, is_forest_green, is_black, is_purple


class ColorsFunctions(AttributesFunctions):
    is_functions = IS_FUNCTIONS
    contains_functions = CONTAINS_FUNCTIONS
    contains_regex = CONTAINS_REGEXS
    attribute_not_exists_exception = ColorNotExists
    invalid_attribute_list_exception = InvalidColorsList


def all_are_colors(container):
    return ColorsFunctions.all_are(container)


def compare_colors(certify_1: str, certify_2: str) -> bool:
    return ColorsFunctions.compare(certify_1, certify_2)


def contains_colors(string: str) -> bool:
    return ColorsFunctions.contains(string)


def has_color(string: str, container: list) -> bool:
    return ColorsFunctions.has(string, container)


def get_color_in_string(string: str) -> str:
    return ColorsFunctions.get_in_string(string)


def get_hex_colors(color: str) -> str:
    if is_crimson(color):
        return "#ff4d4d"
    elif is_sky_blue(color):
        return "#69ffff"
    elif is_pink(color):
        return "#ff8dce"
    elif is_orange(color):
        return "#da9a00"
    elif is_cobalt(color):
        return "#8c9eff"
    elif is_burnt_sienna(color):
        return "#995e4d"
    elif is_titanium_white(color):
        return "#fff"
    elif is_grey(color):
        return "#c4c4c4"
    elif is_saffron(color):
        return "#ff8"
    elif is_lime(color):
        return "#ccff4d"
    elif is_forest_green(color):
        return "#329536"
    elif is_black(color):
        return "#000"
    elif is_purple(color):
        return "#e974fd"


def get_respective_color(color, colors=COLORS):
    return ColorsFunctions.get_respective(color, colors)


def is_color(string: str) -> bool:
    return ColorsFunctions.is_(string)


def validate_color(string):
    return ColorsFunctions.validate(string)


def validate_colors_list(container):
    return ColorsFunctions.validate_list(container)
