from typing import Union, Literal, Optional, Tuple, TypeVar

from rl_data_utils.exceptions import RarityNotExists, RarityIsNotInString
from rl_data_utils.item.attribute.attribute_dict import AttributeDict
from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedAttribute, SetRegexBasedAttribute
from rl_data_utils.item.attribute.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.attribute_string.regex_based_attribute_string import RegexBasedAttributeString
from rl_data_utils.item.rarity.constants import *
from rl_data_utils.item.rarity.regexs import CONTAINS

RarityPatternKey = Literal["Black market", "Common", "Exotic", "Import", "Legacy", "Limited", "Premium", "Rare",
                           "Uncommon", "Very rare"]


Transparency = TypeVar('Transparency')


class RarityInfo(AttributeInfo):
    attribute_name: Final[str] = 'rarity'
    order: Final[int] = 3


class Rarity(RegexBasedAttribute, RarityInfo):
    _attribute_not_exists_exception = RarityNotExists
    _is_reg = CONTAINS
    constants = RARITIES

    def get_rgba(self, tranparency: Transparency) -> Tuple[int, int, int, Transparency]:
        rgb = RarityDict({
            RARE: (116, 151, 235),
            VERY_RARE: (158, 124, 252),
            IMPORT: (227, 90, 82),
            EXOTIC: (236, 219, 108),
            BLACK_MARKET: (255, 0, 255),
            PREMIUM: (107, 241, 174),
            LIMITED: (247, 121, 57)})
        return rgb[self.attribute] + tranparency

    def is_exactly(self, pattern_key: RarityPatternKey) -> bool:
        return super().is_exactly(pattern_key)


Rarity.default_value = Rarity.undefined_value


InitializeRarity = Union[Rarity, str, None]

SetRarities = Optional[List[InitializeRarity]]


class Rarities(RegexBasedListAttribute, RarityInfo):
    sub_attribute = Rarity
    default_value = RARITIES


class RarityDict(AttributeDict):
    _cls_attribute = Rarity
    _cls_list_attribute = Rarities


class RarityString(RegexBasedAttributeString, RarityInfo):
    attribute_class = Rarity
    attributes_class = Rarities
    contains_reg = CONTAINS
    is_not_in_string_exception = RarityIsNotInString


class HasRarity(RarityInfo):
    def __init__(self, rarity: InitializeRarity = None):
        self.rarity: Rarity = rarity

    def get_rarity(self) -> Rarity:
        return self._rarity

    def set_rarity(self, value: SetRegexBasedAttribute):
        self._rarity = Rarity.initialize(value)

    rarity = property(get_rarity, set_rarity)
