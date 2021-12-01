from rl_data_utils.exceptions import PlatformNotExists
from rl_data_utils.item.attribute.str_attribute import StrAttribute
from rl_data_utils.item.platform.platform_info import PlatformInfo
from rl_data_utils.item.platform.regexs import CONTAINS


class Platform(StrAttribute, PlatformInfo):
    _attribute_not_exists_exception = PlatformNotExists
    _is_reg = CONTAINS
