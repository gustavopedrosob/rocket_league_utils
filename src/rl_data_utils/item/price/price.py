from __future__ import annotations

from statistics import mean
from typing import Union, List, Final

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.int_list_attribute import IntListAttribute
from rl_data_utils.item.quantity.credits_quantity import CreditsQuantity


class PriceInfo(AttributeInfo):
    attribute_name: Final[str] = 'price'
    order: Final[int] = 13


class Price(IntListAttribute, PriceInfo):
    sub_attribute = CreditsQuantity

    def get_average(self) -> CreditsQuantity:
        return mean([attr.attribute for attr in self.attribute])

    @classmethod
    def create_random(cls) -> Price:
        return cls([CreditsQuantity.create_random(), CreditsQuantity.create_random()])


InitializePrice = Union[Price, List[int], int, None]
