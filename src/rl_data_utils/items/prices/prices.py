from rl_data_utils.items.items.items import Items
from rl_data_utils.utils.items.prices.prices import get_items_by_price_equal_to, get_items_by_price_lower_than, \
    get_items_by_price_higher_than, get_total_price


class Prices(Items):
    def get_items_by_price_equal_to(self, price: int):
        return self.__class__(get_items_by_price_equal_to(self.items, price))

    def get_items_by_price_lower_than(self, price: int):
        return self.__class__(get_items_by_price_lower_than(self.items, price))

    def get_items_by_price_higher_than(self, price: int):
        return self.__class__(get_items_by_price_higher_than(self.items, price))

    def get_total_price(self) -> int:
        return get_total_price(self.items)
