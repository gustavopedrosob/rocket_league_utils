from rl_data_utils.items.items.items import Items
from rl_data_utils.utils.items.tradables.tradables import get_items_tradable, get_items_not_tradable,\
    get_items_by_tradable


class Tradables(Items):
    def get_items_by_tradable(self, tradable: bool):
        return self.__class__(get_items_by_tradable(tradable, self.items))

    def get_items_tradable(self):
        return self.__class__(get_items_tradable(self.items))

    def get_items_not_tradable(self):
        return self.__class__(get_items_not_tradable(self.items))
