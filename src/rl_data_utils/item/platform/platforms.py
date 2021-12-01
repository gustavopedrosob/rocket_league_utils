from rl_data_utils.item import Platform
from rl_data_utils.item.attribute.str_list_attribute import StrListAttribute
from rl_data_utils.item.platform.platform_info import PlatformInfo


class Platforms(StrListAttribute, PlatformInfo):
    sub_attribute = Platform
