from __future__ import annotations

from random import randint

from rl_data_utils.exceptions import NegativeItemAttribute
from rl_data_utils.item.attribute.int_attribute import IntItemAttribute


class PositiveIntItemAttribute(IntItemAttribute):
    @classmethod
    def create_random(cls):
        return cls(randint(0, 100000))

    def validate(self):
        if self.value is not None:
            if self.value < 0:
                raise NegativeItemAttribute()
