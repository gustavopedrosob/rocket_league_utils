from __future__ import annotations

from abc import ABCMeta
from random import randint

from rl_data_utils.item.attribute.attribute import ItemAttribute


class StaticItemAttribute(ItemAttribute, metaclass=ABCMeta):
    def __init__(self, value):
        self.value = value

    def compare(self, other):
        """
        Compare itself with another attribute
        :param other: An instance of Attribute
        :return: If both are the same attribute
        """
        return self.value == other.value

    @classmethod
    def create_random(cls):
        """
        :return: A self instance from a random value
        """
        return cls(cls.possible_values[randint(0, len(cls.possible_values) - 1)])
