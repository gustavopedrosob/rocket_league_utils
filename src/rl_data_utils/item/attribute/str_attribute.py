from __future__ import annotations

from random import randint
from typing import List, Final, Type, Optional

from rl_data_utils.item.attribute.attribute import Attribute


SetStrAttribute = Optional[str]


class StrAttribute(Attribute):
    attribute_type: Final[Type[str]] = str
    undefined_value: Final[str] = ''
    constants: List[str]

    def __init__(self, attribute: SetStrAttribute):
        super().__init__(attribute)

    @classmethod
    def create_random(cls) -> StrAttribute:
        return cls(cls.constants[randint(0, len(cls.constants)-1)])
