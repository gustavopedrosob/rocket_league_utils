from rl_data_utils.items.items.items import Items
from rl_data_utils.items.tradables.abc_base_tradables import ABCBaseTradables
from rl_data_utils.utils.items.tradables.tradables import get_items_tradable, get_items_not_tradable


class Tradables(ABCBaseTradables, Items):
    def get_items_tradable(self):
        return self.__class__(get_items_tradable(self.items))

    def get_items_not_tradable(self):
        return self.__class__(get_items_not_tradable(self.items))
