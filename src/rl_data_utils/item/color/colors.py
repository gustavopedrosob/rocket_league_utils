from rl_data_utils.item import Color
from rl_data_utils.item.attribute.str_list_attribute import StrListAttribute
from rl_data_utils.item.color.color_info import ColorInfo


class Colors(StrListAttribute, ColorInfo):
    sub_attribute = Color

