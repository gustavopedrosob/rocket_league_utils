from typing import TypedDict, List, Optional

from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.color.color import Color
from rl_data_utils.item.name.name import Name
from rl_data_utils.item.platform.platform import Platform
from rl_data_utils.item.rarity.rarity import Rarity
from rl_data_utils.item.serie.serie import Serie
from rl_data_utils.item.slot.slot import Slot


class T(TypedDict):
    color: Color
    platform: Platform
    serie: Serie
    slot: Slot
    rarity: Rarity
    name: Name


class AttributesString:
    def __init__(self, string: str) -> None:
        self.attributes_strings: List[RegexBasedItemAttribute] = []
        self.string = string
        self.name: Optional[Name] = None

    def get_attributes_dict(self) -> T: ...

    def get_respective_attributes_dict(self) -> T: ...
