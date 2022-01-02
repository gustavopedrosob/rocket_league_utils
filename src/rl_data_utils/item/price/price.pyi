from __future__ import annotations

from typing import Optional

from rl_data_utils.item.attribute.attribute import ItemAttribute
from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.item.constants import PRICE
from rl_data_utils.item.quantity.credits_quantity import CreditsQuantity
from rl_data_utils.rocket_league.rocket_league import Validable


class PriceInfo(AttributeInfo):
    identifier = PRICE
    order = 13


class Price(ItemAttribute, PriceInfo, Validable):
    def __init__(self,
                 min_price: CreditsQuantity,
                 max_price: CreditsQuantity) -> None:
        self.min_price = min_price
        self.max_price = max_price

    def get_average(self) -> Optional[float]: ...

    @classmethod
    def create_random(cls) -> Price: ...

    def validate(self) -> None: ...

    def compare(self, other: Price) -> bool: ...

    def is_valid(self) -> bool: ...
