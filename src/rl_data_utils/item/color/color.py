from abc import abstractmethod, ABC
from rl_data_utils.item.item.item_attribute import ItemAttribute
from rl_data_utils.utils.item.color.color import compare_color, get_hex_colors, get_respective_color, validate_color, \
    is_color, has_color
from rl_data_utils.utils.item.color.is_functions import is_black, is_burnt_sienna, is_cobalt, is_crimson, is_default,\
    is_forest_green, is_grey, is_lime, is_orange, is_pink, is_purple, is_saffron, is_sky_blue, is_titanium_white


class ABCColor(ABC, ItemAttribute):
    def is_valid_color(self):
        return is_color(self.get_color())

    def is_color_in_list(self, colors: list):
        return has_color(self.get_color(), colors)

    def compare_color(self, color) -> bool:
        return compare_color(self.get_color(), color)

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

    @abstractmethod
    def get_color(self):
        pass


class Color(ABCColor):
    def __init__(self, color: str):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color: str):
        self.color = color
