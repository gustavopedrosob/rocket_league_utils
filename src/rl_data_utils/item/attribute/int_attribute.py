from __future__ import annotations

from random import randint

from rl_data_utils.item.attribute.static_attribute import StaticItemAttribute


class IntItemAttribute(StaticItemAttribute):
    @classmethod
    def create_random(cls):
        return cls(randint(-100000, 100000))
