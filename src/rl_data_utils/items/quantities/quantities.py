from rl_data_utils.items.items.items import ABCItems
from rl_data_utils.utils.items.quantities.quantities import get_quantity, get_total_quantity, get_quantities


class ABCQuantities(ABCItems):
    def get_total_quantity(self):
        return get_total_quantity(self.get_items())

    def get_quantity(self):
        return get_quantity(self.get_items())

    def get_quantities(self):
        return get_quantities(self.get_items())
