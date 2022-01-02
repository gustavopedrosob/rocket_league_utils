from __future__ import annotations

from rl_data_utils.item.attribute.attribute_dict import AttributeDict
from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.attribute_data.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.item.constants import RARITY
from rl_data_utils.item.rarity.constants import *
from rl_data_utils.item.rarity.regexs import REGEX_TABLE


class RarityInfo(AttributeInfo):
    identifier = RARITY
    order = 3


class Rarity(RegexBasedItemAttribute, RarityInfo):
    regex_table = REGEX_TABLE
    possible_values = RARITIES

    def get_rgba(self, tranparency):
        return rgb_table[self] + (tranparency,)


class Rarities(RegexBasedListAttribute, RarityInfo):
    attribute_class = Rarity


rgb_table = AttributeDict([
    (Rarity(RARE), (116, 151, 235)),
    (Rarity(VERY_RARE), (158, 124, 252)),
    (Rarity(IMPORT), (227, 90, 82)),
    (Rarity(EXOTIC), (236, 219, 108)),
    (Rarity(BLACK_MARKET), (255, 0, 255)),
    (Rarity(PREMIUM), (107, 241, 174)),
    (Rarity(LIMITED), (247, 121, 57))])
