from typing import Union, Final

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.int_attribute import SetIntAttribute
from rl_data_utils.item.attribute.positive_int_attribute import PositiveIntAttribute


class QuantityInfo(AttributeInfo):
    attribute_name: Final[str] = 'quantity'
    order: Final[int] = -1


class Quantity(PositiveIntAttribute, QuantityInfo):
    pass


InitializeQuantity = Union[Quantity, int, None]


class HasQuantity(QuantityInfo):
    def __init__(self, quantity: InitializeQuantity = None):
        self.quantity: Quantity = quantity

    def get_quantity(self) -> Quantity:
        return self._quantity

    def set_quantity(self, value: SetIntAttribute):
        self._quantity = Quantity.initialize(value)

    quantity = property(get_quantity, set_quantity)
