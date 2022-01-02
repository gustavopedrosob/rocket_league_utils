from __future__ import annotations

from datetime import datetime
from typing import List, Callable

from rl_data_utils.trade.offer import Offer
from rl_data_utils.trade.trade import Trade


class Trades:
    def __init__(self, trades: List[Trade]) -> None:
        self.trades = trades

    def filter_by_trade(self, condition: Callable[[Trade], bool]) -> Trades: ...

    def filter_by_him_offer(self, condition: Callable[[Offer], bool]) -> Trades: ...

    def filter_by_my_offer(self, condition: Callable[[Offer], bool]) -> Trades: ...

    def filter_by_date(self, condition: Callable[[datetime], bool]) -> Trades: ...