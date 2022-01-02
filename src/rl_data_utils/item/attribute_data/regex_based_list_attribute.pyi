from __future__ import annotations

from typing import List, Type, TypeVar, Sequence, Generic

from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.attribute_data.attribute_data import AttributesManagement, AttributesData
from rl_data_utils.item.certified.certified import Certified
from rl_data_utils.item.color.color import Color
from rl_data_utils.item.platform.platform import Platform
from rl_data_utils.item.rarity.rarity import Rarity
from rl_data_utils.item.serie.serie import Serie
from rl_data_utils.item.slot.slot import Slot
from rl_data_utils.rocket_league.rocket_league import FromStrList


RBLAT = TypeVar('RBLAT',
                RegexBasedListAttribute[Color],
                RegexBasedListAttribute[Certified],
                RegexBasedListAttribute[Platform],
                RegexBasedListAttribute[Serie],
                RegexBasedListAttribute[Slot],
                RegexBasedListAttribute[Rarity])
AT = TypeVar('AT', bound=RegexBasedItemAttribute)


class RegexBasedListAttribute(AttributesData, FromStrList, AttributesManagement[AT], Generic[AT]):
    attribute_class: Type[AT]

    def __init__(self, attributes: Sequence[AT]) -> None:
        self.attributes = attributes

    @classmethod
    def from_str_list(cls: Type[RBLAT], str_list: List[str]) -> RBLAT: ...
