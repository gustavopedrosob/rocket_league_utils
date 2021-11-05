from rl_data_utils.color.constants import *
from rl_data_utils.__others import AttributesFunctions
from rl_data_utils.color.is_functions import *
from rl_data_utils.exceptions import InvalidColorsList, ColorNotExists
from rl_data_utils.color.contains import CONTAINS_FUNCTIONS
from rl_data_utils.color.regexs import CONTAINS_REGEXS
from rl_data_utils.color.abc_base_color import ABCBaseColor
from rl_data_utils.item.item_attribute import ItemAttribute


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


def contains_color_in_list(string: str, container: list) -> bool:
    return ColorsFunctions.contains_in_list(string, container)


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


def is_certify_list(container) -> bool:
    return ColorsFunctions.validate_list(container)


def validate_color(string):
    return ColorsFunctions.validate(string)


def validate_colors_list(container):
    return ColorsFunctions.validate_list(container)


class ABCColor(ABCBaseColor, ItemAttribute):
    def compare_colors(self, color) -> bool:
        return compare_colors(self.get_color(), color)

    def get_hex_colors(self):
        return get_hex_colors(self.get_color())

    def get_respective_color(self):
        return get_respective_color(self.get_color())

    def is_black(self) -> bool:
        return is_black(self.get_color())

    def is_burnt_sienna(self) -> bool:
        return is_burnt_sienna(self.get_color())

    def is_cobalt(self) -> bool:
        return is_cobalt(self.get_color())

    def is_crimson(self) -> bool:
        return is_crimson(self.get_color())

    def is_default(self):
        return is_default(self.get_color())

    def is_forest_green(self) -> bool:
        return is_forest_green(self.get_color())

    def is_grey(self) -> bool:
        return is_grey(self.get_color())

    def is_lime(self) -> bool:
        return is_lime(self.get_color())

    def is_orange(self) -> bool:
        return is_orange(self.get_color())

    def is_pink(self) -> bool:
        return is_pink(self.get_color())

    def is_purple(self) -> bool:
        return is_purple(self.get_color())

    def is_saffron(self) -> bool:
        return is_saffron(self.get_color())

    def is_sky_blue(self) -> bool:
        return is_sky_blue(self.get_color())

    def is_titanium_white(self) -> bool:
        return is_titanium_white(self.get_color())

    def validate_color(self):
        validate_color(self.get_color())


class Color(ABCColor):
    def __init__(self, color: str):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color: str):
        self.color = color
