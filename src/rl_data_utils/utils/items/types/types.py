from re import IGNORECASE
from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.items.items.items import get_items_by_condition
from rl_data_utils.item.type.type import ABCType
from rl_data_utils.utils.item.type.type import validate_type, compare_types


def get_items_by_type_regex(type_pattern: str, items: list[ABCType], flags=IGNORECASE):
    return get_items_by_condition(lambda item: _regex_found(type_pattern, item.get_type(), flags), items)


def get_types(items: list[ABCType]):
    return {item.get_type() for item in items}


def get_items_by_type(type_: str, items: list[ABCType]):
    validate_type(type_)
    return get_items_by_condition(lambda item: compare_types(item.get_type(), type_), items)


def get_items_by_type_equal_to(type_: str, items: list[ABCType]):
    return get_items_by_condition(lambda item: item.get_type() == type_, items)


def get_items_by_type_contains(type_: str, items: list[ABCType]):
    return get_items_by_condition(lambda item: type_ in item.get_type(), items)


def get_items_antenna(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_antenna(), items)


def get_items_avatar_border(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_avatar_border(), items)


def get_items_banner(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_banner(), items)


def get_items_boost(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_boost(), items)


def get_items_car(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_car(), items)


def get_items_decal(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_decal(), items)


def get_items_engine_audio(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_engine_audio(), items)


def get_items_gift_pack(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_gift_pack(), items)


def get_items_goal_explosion(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_goal_explosion(), items)


def get_items_paint_finish(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_paint_finish(), items)


def get_items_player_anthem(items: list[ABCType]):
    return get_items_by_condition(lambda item: item.is_player_anthem(), items)


def get_items_topper(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_topper(), items)


def get_items_trail(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_trail(), items)


def get_items_wheel(items: list[ABCType]) -> bool:
    return get_items_by_condition(lambda item: item.is_wheel(), items)
