from rl_data_utils.exceptions import ColorIsNotInString
from rl_data_utils.item.attribute.attribute_string import AttributeString
from rl_data_utils.item.color.color_info import ColorInfo
from rl_data_utils.item.color.regexs import CONTAINS
from rl_data_utils.item.color.color import Color


class ColorString(AttributeString, ColorInfo):
    attribute_class = Color
    contains_reg = CONTAINS
    is_not_in_string_exception = ColorIsNotInString
