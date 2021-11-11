from rl_data_utils.items.items.items import Items
from rl_data_utils.utils.items.quantities.quantities import get_quantity, get_total_quantity, get_quantities


class Quantities(Items):
    def get_total_quantity(self):
        return get_total_quantity(self.items)

    def get_quantity(self):
        return get_quantity(self.items)

    def get_quantities(self):
        return get_quantities(self.items)
