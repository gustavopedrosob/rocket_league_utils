from __future__ import annotations

from typing import Literal, ClassVar

from rl_data_utils.item.attribute.attribute_dict import AttributeDict
from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.attribute_data.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.color.constants import *
from rl_data_utils.rocket_league.rocket_league import Defaultable

ColorPatternKey = Literal["Black", "Burnt Sienna", "Cobalt", "Crimson", "Default", "Forest Green", "Grey",
                          "Lime", "Orange", "Pink", "Purple", "Saffron", "Sky Blue", "Titanium White"]


class ColorInfo(AttributeInfo): ...


class Color(RegexBasedItemAttribute, ColorInfo, Defaultable):
    default_args: ClassVar

    def get_hex(self) -> str: ...


class Colors(RegexBasedListAttribute[Color], ColorInfo): ...


hex_table: AttributeDict[Color, str] = ...
