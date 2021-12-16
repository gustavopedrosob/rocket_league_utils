from __future__ import annotations

from typing import Union, List, Type

from rl_data_utils.item.attribute.int_attribute import IntAttribute
from rl_data_utils.item.attribute.list_attribute import ListAttribute


SetIntListAttribute = Union[List[int], int, None]


class IntListAttribute(ListAttribute):
    sub_attribute: Type[IntAttribute] = IntAttribute

    def __init__(self, attribute: InitializeIntListAttribute = None):
        super().__init__(attribute)


InitializeIntListAttribute = Union[Type[IntListAttribute], List[Type[IntAttribute]], None]
