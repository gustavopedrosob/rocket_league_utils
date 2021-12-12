from typing import List, Union

from rl_data_utils.exceptions import TradeSizeError
from rl_data_utils.item.item.item import Item, InitializeItem
from rl_data_utils.items.items import Items


class TradeItems(Items):
    def _auto_setter(self, value) -> List[Item]:
        if len(value) > 24:
            raise TradeSizeError()
        return super(TradeItems, self)._auto_setter(value)


InitializeTradeItems = Union[TradeItems, List[InitializeItem], None]

