from __future__ import annotations

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.attribute_data.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.item.constants import PLATFORM
from rl_data_utils.item.platform.constants import PLATFORMS
from rl_data_utils.item.platform.regexs import REGEX_TABLE


class PlatformInfo(AttributeInfo):
    identifier = PLATFORM
    order = 6


class Platform(RegexBasedItemAttribute, PlatformInfo):
    regex_table = REGEX_TABLE
    possible_values = PLATFORMS


class Platforms(RegexBasedListAttribute, PlatformInfo):
    attribute_class = Platform
