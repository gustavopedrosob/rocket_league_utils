from __future__ import annotations

from random import randint
from typing import Final, Type, Optional

from rl_data_utils.item.attribute.attribute import Attribute
from rl_data_utils.item.attribute.attribute_info import AttributeInfo

SetIntAttribute = Optional[int]


class IntAttribute(Attribute, AttributeInfo):
    attribute_type: Final[Type[int]] = int
    undefined_value: Final[int] = 0

    def __init__(self, attribute: SetIntAttribute):
        super().__init__(attribute)

    @classmethod
    def create_random(cls) -> IntAttribute:
        return cls(randint(-100000, 100000))
