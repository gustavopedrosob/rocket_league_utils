from rl_data_utils.exceptions import ColorNotExists
from rl_data_utils.item.attribute.str_attribute import StrAttribute
from rl_data_utils.item.color.color_info import ColorInfo
from rl_data_utils.item.color.regexs import CONTAINS


class Color(StrAttribute, ColorInfo):
    _attribute_not_exists_exception = ColorNotExists
    _is_reg = CONTAINS
