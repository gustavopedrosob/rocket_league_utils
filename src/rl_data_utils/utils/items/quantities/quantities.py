from rl_data_utils.item.quantity.quantity import ABCQuantity
from rl_data_utils.utils.items.items.items import get_items_by_condition


def get_items_by_quantity_equal_to(items: list[ABCQuantity], quantity: int):
    return get_items_by_condition(lambda item: item.get_average_quantity() == quantity, items)


def get_items_by_quantity_lower_than(items: list[ABCQuantity], quantity: int):
    return get_items_by_condition(lambda item: item.get_average_quantity() == quantity, items)


def get_items_by_quantity_higher_than(items: list[ABCQuantity], quantity: int):
    return get_items_by_condition(lambda item: item.get_average_quantity() == quantity, items)


def get_quantity(items: list[ABCQuantity]):
    return len(items)


def get_total_quantity(items: list[ABCQuantity]):
    return sum(items)


def get_quantities(items: list[ABCQuantity]) -> list[int]:
    return [item.get_quantity() for item in items]
