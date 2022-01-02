from __future__ import annotations

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.regex_based_attribute import RegexBasedItemAttribute
from rl_data_utils.item.attribute_data.regex_based_list_attribute import RegexBasedListAttribute
from rl_data_utils.item.item.constants import SLOT
from rl_data_utils.item.slot.constants import SLOTS
from rl_data_utils.item.slot.regexs import REGEX_TABLE


class SlotInfo(AttributeInfo):
    identifier = SLOT
    order = 2


class Slot(RegexBasedItemAttribute, SlotInfo):
    regex_table = REGEX_TABLE
    possible_values = SLOTS


class Slots(RegexBasedListAttribute, SlotInfo):
    attribute_class = Slot
