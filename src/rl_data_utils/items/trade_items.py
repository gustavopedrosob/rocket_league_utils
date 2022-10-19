from typing import List, Union

from rl_data_utils.exceptions import TradeSizeError
from rl_data_utils.item.item.item import Item, Credits
from rl_data_utils.items.inventory import Inventory
from rl_data_utils.rocket_league.rocket_league import TradeAttribute


class TradeInventory(Inventory, TradeAttribute):
    def __init__(self, items: List[Item], credits_: Union[Credits, int, None] = None):
        super().__init__(items)
        self.credits = credits_

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, credits_: Union[Credits, int, None]):
        if isinstance(credits_, Credits) or credits_ is None:
            self._credits = credits_
        elif isinstance(credits_, int):
            self._credits = Credits(credits_)
        else:
            raise TypeError("Invalid type for credits property.")

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items: List[Item]):
        if len(items) > 24:
            raise TradeSizeError()
        else:
            self._items = items
