from typing import Union, Literal, Final, Optional, List

from rl_data_utils.exceptions import PlatformNotExists, PlatformIsNotInString
from rl_data_utils.item.attribute.attribute_dict import AttributeDict
from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedAttribute
from rl_data_utils.item.attribute.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.attribute_string.regex_based_attribute_string import RegexBasedAttributeString
from rl_data_utils.item.platform.constants import PLATFORMS
from rl_data_utils.item.platform.regexs import CONTAINS


PlatformPatternKey = Literal['Pc', 'Ps4', 'Switch', 'Xbox']


class PlatformInfo(AttributeInfo):
    attribute_name: Final[str] = 'platform'
    order: Final[int] = 6


class Platform(RegexBasedAttribute, PlatformInfo):
    _attribute_not_exists_exception = PlatformNotExists
    _is_reg = CONTAINS
    constants = PLATFORMS


Platform.default_value = Platform.undefined_value

InitializePlatform = Union[Platform, str, None]

SetPlatforms = Optional[List[InitializePlatform]]


class Platforms(RegexBasedListAttribute, PlatformInfo):
    sub_attribute = Platform


class PlatformDict(AttributeDict):
    _cls_attribute = Platform
    _cls_list_attribute = Platforms


class PlatformString(RegexBasedAttributeString, PlatformInfo):
    attribute_class = Platform
    attributes_class = Platforms
    contains_reg = CONTAINS
    is_not_in_string_exception = PlatformIsNotInString



