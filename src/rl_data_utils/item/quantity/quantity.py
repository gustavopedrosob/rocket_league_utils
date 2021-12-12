from typing import Union, Final

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.positive_int_attribute import PositiveIntAttribute


class QuantityInfo(AttributeInfo):
    attribute_name: Final[str] = 'quantity'
    order: Final[int] = 1


class Quantity(PositiveIntAttribute, QuantityInfo):
    pass


InitializeQuantity = Union[Quantity, int, None]
