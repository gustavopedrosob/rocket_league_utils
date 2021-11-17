from rl_data_utils.item.price.price import ABCPrice
from rl_data_utils.utils.items.items.items import get_items_by_condition


def get_items_by_price_equal_to(items: list[ABCPrice], price: int):
    return get_items_by_condition(lambda item: item.get_average_price() == price, items)


def get_items_by_price_lower_than(items: list[ABCPrice], price: int):
    return get_items_by_condition(lambda item: item.get_average_price() == price, items)


def get_items_by_price_higher_than(items: list[ABCPrice], price: int):
    return get_items_by_condition(lambda item: item.get_average_price() == price, items)


def get_total_price(items: list[ABCPrice]) -> int:
    return sum(get_average_prices(items))


def get_average_prices(items: list[ABCPrice]) -> list[int]:
    return [item for item in items]
