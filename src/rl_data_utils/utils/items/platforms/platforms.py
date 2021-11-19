from re import IGNORECASE
from rl_data_utils.__others import _regex_found
from rl_data_utils.item.platform.platform import ABCPlatform
from rl_data_utils.utils.items.items.items import get_items_by_condition


def get_items_pc(items: list[ABCPlatform]):
    return get_items_by_condition(lambda item: item.is_pc(), items)


def get_items_ps4(items: list[ABCPlatform]):
    return get_items_by_condition(lambda item: item.is_ps4(), items)


def get_items_xbox(items: list[ABCPlatform]):
    return get_items_by_condition(lambda item: item.is_xbox(), items)


def get_items_switch(items: list[ABCPlatform]):
    return get_items_by_condition(lambda item: item.is_switch(), items)


def get_items_with_valid_platform(items: list[ABCPlatform]):
    return get_items_by_condition(lambda item: item.is_valid_platform(), items)


def get_items_by_platform_regex(items: list[ABCPlatform], platform_pattern, flags=IGNORECASE):
    return get_items_by_condition(lambda item: _regex_found(platform_pattern, item.get_platform(), flags), items)


def get_items_by_platform(items: list[ABCPlatform], platform: str):
    return get_items_by_condition(lambda item: item.compare_platforms(platform), items)


def get_items_by_platform_equal_to(items: list[ABCPlatform], platform: str):
    return get_items_by_condition(lambda item: item.get_platform() == platform, items)


def get_items_by_platform_contains(items: list[ABCPlatform], platform: str):
    return get_items_by_condition(lambda item: platform in item.get_platform(), items)


def get_platforms(items: list[ABCPlatform]):
    return set(map(lambda item: item.get_platform(), items))
