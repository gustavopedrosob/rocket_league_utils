from re import IGNORECASE
from rl_data_utils.__others import _regex_found
from rl_data_utils.item.rarity.rarity import ABCRarity
from rl_data_utils.utils.items.items.items import get_items_by_condition


def get_items_with_valid_rarity(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_valid_rarity(), items)


def get_rarities(items: list[ABCRarity]):
    return {item.get_rarity() for item in items}


def get_items_by_rarity_regex(rarity_pattern: str, items: list[ABCRarity], flags=IGNORECASE):
    return get_items_by_condition(lambda item: _regex_found(rarity_pattern, item.get_rarity(), flags), items)


def get_items_by_rarity(rarity: str, items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.compare_rarity(rarity), items)


def get_items_by_rarity_equal_to(rarity: str, items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.get_rarity() == rarity, items)


def get_items_by_rarity_contains(rarity: str, items: list[ABCRarity]):
    return get_items_by_condition(lambda item: rarity in item.get_rarity(), items)


def get_items_common(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_common(), items)


def get_items_legacy(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_legacy(), items)


def get_items_uncommon(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_uncommon(), items)


def get_items_rare(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_rare(), items)


def get_items_very_rare(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_very_rare(), items)


def get_items_import(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_import(), items)


def get_items_exotic(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_exotic(), items)


def get_items_black_market(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_black_market(), items)


def get_items_limited(items: list[ABCRarity]):
    return get_items_by_condition(lambda item: item.is_limited(), items)