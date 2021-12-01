from rl_data_utils.exceptions import SlotIsNotInString
from rl_data_utils.item.attribute.attribute_string import AttributeString
from rl_data_utils.item.slot.regexs import CONTAINS
from rl_data_utils.item.slot.slot import Slot
from rl_data_utils.item.slot.slot_info import SlotInfo


class SlotString(AttributeString, SlotInfo):
    attribute_class = Slot
    contains_reg = CONTAINS
    is_not_in_string_exception = SlotIsNotInString
