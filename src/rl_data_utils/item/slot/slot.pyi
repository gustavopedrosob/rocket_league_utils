from __future__ import annotations

from typing import Literal

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.attribute_data.regex_based_list_attribute import RegexBasedListAttribute

SlotPatternKey = Literal["Antenna", "Avatar Border", "Car", 'Blueprint', "Decal", "Engine Audio", "Goal Explosion",
                         "Gift Pack", "Paint Finish", "Anthem", "Banner", "Boost", "Topper", "Trail", "Wheel", 'Title']


class SlotInfo(AttributeInfo): ...


class Slot(RegexBasedItemAttribute, SlotInfo): ...


class Slots(RegexBasedListAttribute[Slot], SlotInfo): ...
