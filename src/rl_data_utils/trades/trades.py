from __future__ import annotations

from collections import Callable
from typing import Optional, List

from rl_data_utils.trade.trade import Trade


class Trades:
    def __init__(self, trades: Optional[List[Trade]]):
        self.trades: List[Trade] = trades

    def __repr__(self) -> str:
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
                    raise TypeError('Invalid type, expected Trade.')
        else:
            raise TypeError('Invalid type, expected List[Trade].')

    def filter_by_trade_condition(self, condition: Callable[[Trade], bool]) -> Trades:
        """
        Filter self trades by a condition function that receives a trade as parameter and returns a boolean
        :param condition: A function that works as condition, receives a trade as parameter and return a boolean
        :return: A filtered trades instance
        """
        return self.__class__(list(filter(condition, self.trades)))

