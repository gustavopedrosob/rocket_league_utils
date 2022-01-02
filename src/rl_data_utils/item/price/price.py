from __future__ import annotations

from statistics import mean

from rl_data_utils.exceptions import InvalidItemAttribute
from rl_data_utils.item.attribute.attribute import ItemAttribute
from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.item.constants import PRICE
from rl_data_utils.item.quantity.credits_quantity import CreditsQuantity
from rl_data_utils.rocket_league.rocket_league import Validable


class PriceInfo(AttributeInfo):
    identifier = PRICE
    order = 13


class Price(ItemAttribute, PriceInfo, Validable):
    def __init__(self, min_price, max_price):
        self.min_price = min_price
        self.max_price = max_price

    def get_average(self):
        return mean([self.min_price.value, self.max_price.value])

    @classmethod
    def create_random(cls):
        return cls(CreditsQuantity.create_random(), CreditsQuantity.create_random())

    def validate(self):
        self.min_price.validate()
        self.max_price.validate()

    def compare(self, other: Price):
        return self.max_price.compare(other.max_price) and self.min_price.compare(other.min_price)

    def is_valid(self):
        return self._is_valid_by_validate(InvalidItemAttribute)
