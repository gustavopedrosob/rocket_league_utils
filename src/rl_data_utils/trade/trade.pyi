from datetime import datetime
from typing import Literal, Optional

from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject
from rl_data_utils.trade.offer import Offer


class Trade(RocketLeagueObject):
    def __init__(self, my_offer: Offer, him_offer: Offer, date: Optional[datetime] = ...):
        self.him_offer = him_offer
        self.my_offer = my_offer
        self.date = date

    def is_sale(self) -> bool: ...

    def is_buy(self) -> bool: ...

    def is_item_by_item(self) -> bool: ...

    def validate(self) -> None: ...

    def get_type(self) -> Literal['sale', 'buy', 'item-by-item']: ...

    def is_valid(self) -> bool: ...
