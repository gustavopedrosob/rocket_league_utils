from rl_data_utils.item.paintable.paintable import ABCPaintable
from rl_data_utils.utils.items.items.items import get_items_by_condition


def get_items_by_paintable(paintable: bool, items: list[ABCPaintable]):
    return get_items_by_condition(lambda item: item.get_paintable() == paintable, items)


def get_items_paintable(items: list[ABCPaintable]):
    return get_items_by_condition(lambda item: item.get_paintable(), items)


def get_items_not_paintable(items: list[ABCPaintable]):
    return get_items_by_condition(lambda item: not item.get_paintable(), items)