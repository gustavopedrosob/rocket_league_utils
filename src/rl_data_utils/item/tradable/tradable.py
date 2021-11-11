from rl_data_utils.item.item.item_attribute import ItemAttribute
from rl_data_utils.item.tradable.abc_base_tradable import ABCBaseTradable


class ABCTradable(ABCBaseTradable, ItemAttribute):
    pass


class Tradable(ABCTradable):
    def __init__(self, tradable: bool):
        self.tradable = tradable

    def get_tradable(self) -> bool:
        return self.tradable
