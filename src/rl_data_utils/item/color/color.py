from __future__ import annotations

from rl_data_utils.item.attribute.attribute_dict import AttributeDict
from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.attribute_data.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.color.constants import *
from rl_data_utils.item.color.regexs import REGEX_TABLE
from rl_data_utils.item.item.constants import COLOR
from rl_data_utils.rocket_league.rocket_league import Defaultable


class ColorInfo(AttributeInfo):
    identifier = COLOR
    order = 4


class Color(RegexBasedItemAttribute, ColorInfo, Defaultable):
    regex_table = REGEX_TABLE
    possible_values = COLORS
    default_args = [DEFAULT], dict()

    def get_hex(self):
        return hex_table[self]


class Colors(RegexBasedListAttribute, ColorInfo):
    attribute_class = Color


hex_table = AttributeDict([
    (Color(CRIMSON), "#ff4d4d"),
    (Color(SKY_BLUE), "#69ffff"),
    (Color(PINK), "#ff8dce"),
    (Color(ORANGE), "#da9a00"),
    (Color(COBALT), "#8c9eff"),
    (Color(BURNT_SIENNA), "#995e4d"),
    (Color(TITANIUM_WHITE), "#fff"),
    (Color(GREY), "#c4c4c4"),
    (Color(SAFFRON), "#ff8"),
    (Color(LIME), "#ccff4d"),
    (Color(FOREST_GREEN), "#329536"),
    (Color(BLACK), "#000"),
    (Color(PURPLE), "#e974fd")
])
