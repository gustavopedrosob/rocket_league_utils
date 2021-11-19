from rl_data_utils.items.items.items import Items
from rl_data_utils.utils.items.quantities.quantities import get_quantity, get_total_quantity, get_quantities, \
    get_items_by_quantity_equal_to, get_items_by_quantity_lower_than, get_items_by_quantity_higher_than


class Quantities(Items):
    def get_items_by_quantity_equal_to(self, quantity: int):
        return self.__class__(get_items_by_quantity_equal_to(self.items, quantity))

    def get_items_by_quantity_lower_than(self, quantity: int):
        return self.__class__(get_items_by_quantity_lower_than(self.items, quantity))

    def get_items_by_quantity_higher_than(self, quantity: int):
        return self.__class__(get_items_by_quantity_higher_than(self.items, quantity))

    def get_total_quantity(self) -> int:
        return get_total_quantity(self.items)

    def get_quantity(self):
        return get_quantity(self.items)

    def get_quantities(self):
        return get_quantities(self.items)
