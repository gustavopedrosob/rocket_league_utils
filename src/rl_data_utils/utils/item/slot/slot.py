from rl_data_utils.__others import AttributesFunctions
from rl_data_utils.exceptions import SlotNotExists, InvalidSlotsList, SlotIsNotInString
from rl_data_utils.utils.item.slot.constants import SLOTS
from rl_data_utils.utils.item.slot.contains import CONTAINS_FUNCTIONS
from rl_data_utils.utils.item.slot.is_functions import IS_FUNCTIONS
from rl_data_utils.utils.item.slot.regexs import CONTAINS_REGEXS
from functools import lru_cache


class SlotsFunctions(AttributesFunctions):
    is_functions = IS_FUNCTIONS
    contains_functions = CONTAINS_FUNCTIONS
    contains_regex = CONTAINS_REGEXS
    attribute_not_exists_exception = SlotNotExists
    invalid_attribute_list_exception = InvalidSlotsList
    is_not_in_string_exception = SlotIsNotInString


def all_are_slots(container):
    return SlotsFunctions.all_are(container)


@lru_cache()
def compare_slot(slot_1: str, slot_2: str) -> bool:
    return SlotsFunctions.compare(slot_1, slot_2)


def contains_slots(string: str) -> bool:
    return SlotsFunctions.contains(string)


def has_slot(string: str, container: list) -> bool:
    return SlotsFunctions.has(string, container)


def get_respective_slot(slot, slots=SLOTS):
    return SlotsFunctions.get_respective(slot, slots)


def get_slot_in_string(string: str) -> str:
    return SlotsFunctions.get_in_string(string)


def is_slot(string: str) -> bool:
    return SlotsFunctions.is_(string)


def validate_slot(string):
    return SlotsFunctions.validate(string)


def validate_slots_list(container):
    return SlotsFunctions.validate_list(container)
