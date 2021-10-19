from rocket_league_utils.colors.isandcompare import ColorIsAndCompare
from rocket_league_utils.colors.constants import *
from rocket_league_utils.colors.is_functions import *


def compare_colors(color_1: str, color_2: str) -> bool:
    return ColorIsAndCompare.compare_(color_1, color_2)


def is_color(string: str) -> bool:
    return ColorIsAndCompare.is_(string)


def get_respective_color(color: str) -> str:
    if is_default(color):
        return DEFAULT
    elif is_crimson(color):
        return CRIMSON
    elif is_sky_blue(color):
        return SKY_BLUE
    elif is_pink(color):
        return PINK
    elif is_orange(color):
        return ORANGE
    elif is_cobalt(color):
        return COBALT
    elif is_burnt_sienna(color):
        return BURNT_SIENNA
    elif is_titanium_white(color):
        return TITANIUM_WHITE
    elif is_grey(color):
        return GREY
    elif is_saffron(color):
        return SAFFRON
    elif is_lime(color):
        return LIME
    elif is_forest_green(color):
        return FOREST_GREEN
    elif is_black(color):
        return BLACK
    elif is_purple(color):
        return PURPLE


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


class Color:
    def __init__(self, color: str):
        self.color = color

    def is_black(self) -> bool:
        return is_black(self.color)

    def is_titanium_white(self) -> bool:
        return is_titanium_white(self.color)

    def is_grey(self) -> bool:
        return is_grey(self.color)

    def is_crimson(self) -> bool:
        return is_crimson(self.color)

    def is_pink(self) -> bool:
        return is_pink(self.color)

    def is_cobalt(self) -> bool:
        return is_cobalt(self.color)

    def is_sky_blue(self) -> bool:
        return is_sky_blue(self.color)

    def is_burnt_sienna(self) -> bool:
        return is_burnt_sienna(self.color)

    def is_saffron(self) -> bool:
        return is_saffron(self.color)

    def is_lime(self) -> bool:
        return is_lime(self.color)

    def is_forest_green(self) -> bool:
        return is_forest_green(self.color)

    def is_orange(self) -> bool:
        return is_orange(self.color)

    def is_purple(self) -> bool:
        return is_purple(self.color)

    def compare_color(self, color) -> bool:
        return compare_colors(self.color, color)

    def get_respective_color(self):
        return get_respective_color(self.color)

    def get_hex_colors(self):
        return get_hex_colors(self.color)
