from rl_data_utils.exceptions import TradeSizeError
from rl_data_utils.items.items import Items


class TradeItems(Items):
    def _auto_setter(self, value):
        if len(value) > 24:
            raise TradeSizeError()
        return super(TradeItems, self)._auto_setter(value)
