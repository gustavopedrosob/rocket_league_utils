from __future__ import annotations

from random import randint

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.int_attribute import IntAttribute


class PositiveIntAttribute(IntAttribute, AttributeInfo):
    def _auto_setter(self, value: int) -> int:
        if isinstance(value, int):
            if value < 0:
                raise ValueError('Invalid value, it can\'t be negative.')
        return super()._auto_setter(value)

    @classmethod
    def create_random(cls) -> PositiveIntAttribute:
        return cls(randint(0, 100000))
