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
