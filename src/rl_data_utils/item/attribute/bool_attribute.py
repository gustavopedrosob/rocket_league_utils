from __future__ import annotations

from random import randint

from typing import Final, Type, Optional

from rl_data_utils.item.attribute.attribute import Attribute
from rl_data_utils.item.attribute.attribute_info import AttributeInfo

SetBoolAttribute = Optional[bool]


class BoolAttribute(Attribute, AttributeInfo):
    attribute_type: Final[Type[bool]] = bool
    undefined_value: Final[None] = None

    def __init__(self, attribute: SetBoolAttribute):
        super().__init__(attribute)

    @classmethod
    def create_random(cls) -> BoolAttribute:
        return cls([True, False][randint(0, 1)])
