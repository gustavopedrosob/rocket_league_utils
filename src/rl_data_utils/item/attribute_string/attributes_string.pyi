from typing import TypedDict, List, Optional

from rl_data_utils.item.attribute.attribute import Color, Name, Platform, Rarity, Serie, Slot, RegexBasedItemAttribute


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
