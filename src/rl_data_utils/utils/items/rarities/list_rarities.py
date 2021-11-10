from re import IGNORECASE

from rl_data_utils.__others import _regex_found_any_in_list
from rl_data_utils.item.rarity.list_rarity import ABCListRarity
from rl_data_utils.utils.item.rarity.rarity import has_rarity
from rl_data_utils.utils.items.items.items import get_items_by_condition


def get_items_by_rarity(rarity: str, items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: has_rarity(rarity, item.get_list_rarity()),
                                  items)


def get_items_by_rarity_regex(rarity_pattern: str, items: list[ABCListRarity], flags=IGNORECASE):
    return get_items_by_condition(
        lambda item: _regex_found_any_in_list(rarity_pattern, item.get_list_rarity(), flags), items)


def get_items_by_rarity_equal_to(rarity: str, items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: rarity in item.get_list_rarity(), items)


def get_items_by_rarity_contains(rarity: str, items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: any([rarity in ri for ri in item.get_list_rarity()]), items)


def get_items_rare(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_rare(), items)


def get_items_very_rare(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_very_rare(), items)


def get_items_import(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_import(), items)


def get_items_exotic(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_exotic(), items)


def get_items_black_market(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_black_market(), items)


def get_items_limited(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_limited(), items)


def get_items_uncommon(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_uncommon(), items)


def get_items_common(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_common(), items)


def get_items_legacy(items: list[ABCListRarity]):
    return get_items_by_condition(lambda item: item.has_legacy(), items)