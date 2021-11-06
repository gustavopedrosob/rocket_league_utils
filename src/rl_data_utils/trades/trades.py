from rl_data_utils.trade.trade import ABCTrade
from rl_data_utils.__others import filter_container_by_condition
from abc import ABC, abstractmethod


def get_trades_by_condition(lamb, trades: list[ABCTrade]) -> list[ABCTrade]:
    return filter_container_by_condition(lamb, trades)


def get_buy_trades(trades: list[ABCTrade]):
    return get_trades_by_condition(lambda trade: trade.is_buy(), trades)


def get_sale_trades(trades: list[ABCTrade]):
    return get_trades_by_condition(lambda trade: trade.is_sale(), trades)


class ABCTrades(ABC):
    @abstractmethod
    def get_trades(self) -> list[ABCTrade]:
        pass

    def get_buy_trades(self) -> list[ABCTrade]:
        return get_buy_trades(self.get_trades())

    def get_sale_trades(self) -> list[ABCTrade]:
        return get_sale_trades(self.get_trades())
