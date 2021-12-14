from __future__ import annotations

from typing import List, Optional, Callable

from rl_data_utils.item.attribute.any_attribute import AnyAllAttribute


class AttributeCollection:
    def __init__(self, attributes: Optional[List[AnyAllAttribute]]):
        self.attributes: List[AnyAllAttribute] = attributes

    def __iter__(self):
        for each in self.attributes:
            yield each

    def filter(self, condition: Callable[[AnyAllAttribute], bool]) -> AttributeCollection:
        """
        Get attributes filtered by a function that works as condition
        :param condition: A function that receives an Attribute as argument and returns a boolean
        :return: A filtered list of Attribute
        """
        return self.__class__(list(filter(condition, self.attributes)))

