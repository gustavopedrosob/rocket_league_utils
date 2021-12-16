from __future__ import annotations

from statistics import mean, StatisticsError
from typing import Union, Final, Optional

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.int_list_attribute import IntListAttribute, SetIntListAttribute
from rl_data_utils.item.quantity.credits_quantity import CreditsQuantity


class PriceInfo(AttributeInfo):
    attribute_name: Final[str] = 'price'
    order: Final[int] = 13


SetPrice = SetIntListAttribute


class Price(IntListAttribute, PriceInfo):
    sub_attribute = CreditsQuantity

    def get_average(self) -> int:
        try:
            return mean([attr.attribute for attr in self.attribute])
        except StatisticsError:
            return None

    def get_repr(self, attribute: Optional[str, int] = None, maxsize: Optional[int] = 15):
        if attribute is None:
            attribute = self.get_average()
        return super().get_repr(attribute)

    @classmethod
    def create_random(cls) -> Price:
        return cls([CreditsQuantity.create_random(), CreditsQuantity.create_random()])


InitializePrice = Union[Price, SetPrice]


class HasPrice(PriceInfo):
    def __init__(self, price: InitializePrice = None):
        self.price: Price = price

    def get_price(self) -> Price:
        return self._price

    def set_price(self, value: SetPrice):
        self._price = Price.initialize(value)

    price = property(get_price, set_price)
