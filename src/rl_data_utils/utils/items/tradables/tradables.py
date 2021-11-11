from rl_data_utils.item.tradable.tradable import ABCTradable
from rl_data_utils.utils.items.items.items import get_items_by_condition


def get_items_tradable(items: list[ABCTradable]):
    return get_items_by_condition(lambda item: item.get_tradable(), items)


def get_items_not_tradable(items: list[ABCTradable]):
    return get_items_by_condition(lambda item: not item.get_tradable(), items)
