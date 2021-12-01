from rl_data_utils.exceptions import PlatformIsNotInString
from rl_data_utils.item.attribute.attribute_string import AttributeString
from rl_data_utils.item.platform.platform_info import PlatformInfo
from rl_data_utils.item.platform.regexs import CONTAINS
from rl_data_utils.item.platform.platform import Platform


class PlatformString(AttributeString, PlatformInfo):
    attribute_class = Platform
    contains_reg = CONTAINS
    is_not_in_string_exception = PlatformIsNotInString
