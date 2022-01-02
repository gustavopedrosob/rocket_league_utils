from __future__ import annotations

from typing import Literal, Tuple, TypeVar

from rl_data_utils.item.attribute.attribute_dict import AttributeDict
from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.attribute_data.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.item.constants import RARITY
from rl_data_utils.item.rarity.constants import *
from rl_data_utils.item.rarity.regexs import REGEX_TABLE

RarityPatternKey = Literal["Black market", "Common", "Exotic", "Import", "Legacy", "Limited", "Premium", "Rare",
                           "Uncommon", "Very rare"]


Transparency = TypeVar('Transparency', int, float)


class RarityInfo(AttributeInfo): ...


class Rarity(RegexBasedItemAttribute, RarityInfo):
    def get_rgba(self, tranparency: Transparency) -> Tuple[int, int, int, Transparency]: ...


class Rarities(RegexBasedListAttribute[Rarity], RarityInfo): ...


rgb_table: AttributeDict[Rarity, Tuple[int, int, int]] = ...
