from re import IGNORECASE
from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.items.items.items import get_items_by_condition
from rl_data_utils.item.slot.slot import ABCSlot


def get_items_with_valid_slot(items: list[ABCSlot]):
    return get_items_by_condition(lambda item: item.is_valid_slot(), items)


def get_items_by_slot_regex(slot: str, items: list[ABCSlot], flags=IGNORECASE):
    return get_items_by_condition(lambda item: _regex_found(slot, item.get_slot(), flags), items)


def get_slots(items: list[ABCSlot]):
    return {item.get_slot() for item in items}


def get_items_by_slot(slot: str, items: list[ABCSlot]):
    return get_items_by_condition(lambda item: item.compare_slot(slot), items)


def get_items_by_slot_equal_to(slot: str, items: list[ABCSlot]):
    return get_items_by_condition(lambda item: item.get_slot() == slot, items)


def get_items_by_slot_contains(slot: str, items: list[ABCSlot]):
    return get_items_by_condition(lambda item: slot in item.get_slot(), items)


def get_items_antenna(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_antenna(), items)


def get_items_avatar_border(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_avatar_border(), items)


def get_items_banner(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_banner(), items)


def get_items_blueprint(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_blueprint(), items)


def get_items_boost(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_boost(), items)


def get_items_car(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_car(), items)


def get_items_decal(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_decal(), items)


def get_items_engine_audio(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_engine_audio(), items)


def get_items_gift_pack(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_gift_pack(), items)


def get_items_goal_explosion(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_goal_explosion(), items)


def get_items_paint_finish(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_paint_finish(), items)


def get_items_player_anthem(items: list[ABCSlot]):
    return get_items_by_condition(lambda item: item.is_player_anthem(), items)


def get_items_player_title(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_player_title(), items)


def get_items_topper(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_topper(), items)


def get_items_trail(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_trail(), items)


def get_items_wheel(items: list[ABCSlot]) -> bool:
    return get_items_by_condition(lambda item: item.is_wheel(), items)
