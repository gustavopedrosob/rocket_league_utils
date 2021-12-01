from rl_data_utils.item.item.item import Item
from rl_data_utils.trade.trade import Trade


class Trades:
    def __init__(self, trades):
        self.trades = trades

    def __repr__(self):
        return '\n'.join([repr(trade) for trade in self.trades])

    @property
    def trades(self):
        return self._trades

    @trades.setter
    def trades(self, value):
        if value is None or value == []:
            self._trades = []
        elif isinstance(value, list):
            self._trades = value
            for trade in value:
                if not isinstance(trade, Trade):
                    raise TypeError()
        else:
            raise TypeError()

    def filter_by_trade(self, condition):
        return self.__class__(list(filter(condition, self.trades)))

    def filter_trades(self):
        return self.filter_by_trade(lambda trade: trade.is_item_by_item())

    def filter_sales(self):
        return self.filter_by_trade(lambda trade: trade.is_sale())

    def filter_buys(self):
        return self.filter_by_trade(lambda trade: trade.is_buy())

    def filter_by_him_item(self, item):
        item = Item.initialize(item)
        return self.filter_by_trade(lambda trade: not trade.him_items.filter_by(item).is_undefined())

    def filter_by_my_item(self, item):
        item = Item.initialize(item)
        return self.filter_by_trade(lambda trade: not trade.my_items.filter_by(item).is_undefined())
