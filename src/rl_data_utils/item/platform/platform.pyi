from __future__ import annotations

from typing import Literal

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.attribute_data.regex_based_list_attribute import RegexBasedListAttribute

PlatformPatternKey = Literal['Pc', 'Ps4', 'Switch', 'Xbox']


class PlatformInfo(AttributeInfo): ...


class Platform(RegexBasedItemAttribute, PlatformInfo): ...


class Platforms(RegexBasedListAttribute[Platform], PlatformInfo): ...
