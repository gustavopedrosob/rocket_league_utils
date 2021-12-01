from rl_data_utils.exceptions import SlotNotExists
from rl_data_utils.item.attribute.str_attribute import StrAttribute
from rl_data_utils.item.slot.regexs import CONTAINS
from rl_data_utils.item.slot.slot_info import SlotInfo


class Slot(StrAttribute, SlotInfo):
    _is_reg = CONTAINS
    _attribute_not_exists_exception = SlotNotExists
