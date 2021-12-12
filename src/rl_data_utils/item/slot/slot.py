from typing import Union, Literal, Final, Optional, List

from rl_data_utils.exceptions import SlotNotExists, SlotIsNotInString
from rl_data_utils.item.attribute.attribute_dict import AttributeDict
from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedAttribute
from rl_data_utils.item.attribute.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.attribute_string.regex_based_attribute_string import RegexBasedAttributeString
from rl_data_utils.item.slot.constants import SLOTS
from rl_data_utils.item.slot.regexs import CONTAINS

SlotPatternKey = Literal["Antenna", "Avatar Border", "Car", 'Blueprint', "Decal", "Engine Audio", "Goal Explosion",
                         "Gift Pack", "Paint Finish", "Anthem", "Banner", "Boost", "Topper", "Trail", "Wheel", 'Title']


class SlotInfo(AttributeInfo):
    attribute_name: Final[str] = 'slot'
    order: Final[int] = 2


class Slot(RegexBasedAttribute, SlotInfo):
    _is_reg = CONTAINS
    _attribute_not_exists_exception = SlotNotExists
    constants = SLOTS


Slot.default_value = Slot.undefined_value


InitializeSlot = Union[Slot, str, None]


SetSlots = Optional[List[InitializeSlot]]


class Slots(RegexBasedListAttribute, SlotInfo):
    sub_attribute = Slot
    default_value = SLOTS


class SlotDict(AttributeDict):
    _cls_attribute = Slot
    _cls_list_attribute = Slots


class SlotString(RegexBasedAttributeString, SlotInfo):
    attribute_class = Slot
    attributes_class = Slots
    contains_reg = CONTAINS
    is_not_in_string_exception = SlotIsNotInString
