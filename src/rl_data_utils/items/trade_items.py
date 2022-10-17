from typing import List

from rl_data_utils.exceptions import TradeSizeError
from rl_data_utils.items.items import Items
from rl_data_utils.rocket_league.rocket_league import TradeAttribute


class TradeItems(Items, TradeAttribute):
    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items: List[Items]):
        if len(items) > 24:
            raise TradeSizeError()
        else:
            self._items = items
