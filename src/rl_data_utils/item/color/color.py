from typing import Union, Literal, Optional

from rl_data_utils.exceptions import ColorNotExists, ColorIsNotInString
from rl_data_utils.item.attribute.attribute_dict import AttributeDict
from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedAttribute
from rl_data_utils.item.attribute.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.attribute_string.regex_based_attribute_string import RegexBasedAttributeString
from rl_data_utils.item.color.constants import *
from rl_data_utils.item.color.regexs import CONTAINS

ColorPatternKey = Literal["Black", "Burnt Sienna", "Cobalt", "Crimson", "Default", "Forest Green", "Grey",
                          "Lime", "Orange", "Pink", "Purple", "Saffron", "Sky Blue", "Titanium White"]


class ColorInfo(AttributeInfo):
    attribute_name: Final[str] = 'color'
    order: Final[int] = 4


class Color(RegexBasedAttribute, ColorInfo):
    _attribute_not_exists_exception = ColorNotExists
    _is_reg = CONTAINS
    constants = COLORS

    def get_hex(self) -> str:
        _hex = ColorDict({
            CRIMSON: "#ff4d4d",
            SKY_BLUE: "#69ffff",
            PINK: "#ff8dce",
            ORANGE: "#da9a00",
            COBALT: "#8c9eff",
            BURNT_SIENNA: "#995e4d",
            TITANIUM_WHITE: "#fff",
            GREY: "#c4c4c4",
            SAFFRON: "#ff8",
            LIME: "#ccff4d",
            FOREST_GREEN: "#329536",
            BLACK: "#000",
            PURPLE: "#e974fd"
        })
        return _hex[self.attribute]


Color.default_value = Color.undefined_value


InitializeColor = Union[Color, str, None]

SetColors = Optional[List[InitializeColor]]


class Colors(RegexBasedListAttribute, ColorInfo):
    sub_attribute = Color
    default_value = COLORS


class ColorDict(AttributeDict):
    _cls_attribute = Color
    _cls_list_attribute = Colors


class ColorString(RegexBasedAttributeString, ColorInfo):
    attribute_class = Color
    attributes_class = Colors
    contains_reg = CONTAINS
    is_not_in_string_exception = ColorIsNotInString
