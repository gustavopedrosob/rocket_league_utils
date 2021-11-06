from rl_data_utils.item.quantity.quantity import ABCQuantity


def get_quantity(items: list[ABCQuantity]):
    return len(items)


def get_total_quantity(items: list[ABCQuantity]):
    return sum(items)


def get_quantities(items: list[ABCQuantity]) -> list[int]:
    return [item.get_quantity() for item in items]
