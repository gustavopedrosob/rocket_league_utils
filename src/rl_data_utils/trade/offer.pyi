from typing import Optional

from rl_data_utils.account.account import Account
from rl_data_utils.item.item.credit import Credit
from rl_data_utils.items.trade_items import TradeItems
from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject, Validable


class Offer(RocketLeagueObject, Validable):
    def __init__(self,
                 credits_: Optional[Credit] = ...,
                 items: Optional[TradeItems] = ...,
                 author: Optional[Account] = ...) -> None:
        self.credits = credits_
        self.items = items
        self.author = author

    def is_only_items(self) -> bool: ...

    def is_only_credits(self) -> bool: ...

    def is_items_and_credits(self) -> bool: ...

    def validate(self) -> None: ...

    def is_valid(self) -> bool: ...
