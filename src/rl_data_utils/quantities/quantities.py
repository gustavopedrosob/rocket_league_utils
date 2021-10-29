from rl_data_utils.items.abc_items import ABCItems
from rl_data_utils.quantity.quantity import ABCQuantity


class ABCQuantities(ABCItems):
    def get_total_quantity(self):
        return get_total_quantity(self.get_items())

    def get_quantity(self):
        return get_quantity(self.get_items())

    def get_quantities(self):
        return get_quantities(self.get_items())


def get_quantity(items: list[ABCQuantity]):
    return len(items)


def get_total_quantity(items: list[ABCQuantity]):
    return sum(items)


def get_quantities(items: list[ABCQuantity]) -> list[int]:
    return [item.get_quantity() for item in items]
