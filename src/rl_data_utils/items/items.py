from __future__ import annotations

from functools import reduce

from rl_data_utils.exceptions import InvalidItemAttribute
from rl_data_utils.item.item.constants import FULL
from rl_data_utils.item.item.item import Item
from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject, Filterable, Validable, CanBeEmpty


class Items(RocketLeagueObject, Filterable, Validable, CanBeEmpty):
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        yield from self.items

    def filter_by_item(self, item: Item, attrs=None):
        """
        Filters self items by an Item, it ignores undefined attributes to filter
        :param item: A item to find in items
        :param attrs: Names of attributes that you want to compare
        :raise AttributeError: If some name in attrs is invalid or the attribute is not in instance
        :raise KeyError: If mode is Invalid
        :return A self instance with items that match with item
        """
        if not attrs:
            attrs = FULL
        attributes = list(filter(lambda attr: attr.identifier in attrs, item.get_attributes()))
        return self.filter_by_attributes(attributes)

    def filter_by_attributes(self, attributes):
        """
        Filters self items by attributes
        :param attributes: Attributes to compare
        :return: A self instance with items that match with attributes
        """
        return reduce(lambda result, attr: result.filter_by_attribute(attr), (self, *attributes))  # type: ignore

    def filter_by_attribute(self, attribute):
        """
        Filters self items by an attribute
        :param attribute: A attribute to find in items
        :return: A self instance with items that match with attribute
        """
        return self.filter_by_condition(
            lambda item: Item.match_attributes(attribute, getattr(item, attribute.identifier)))

    def filter_by_condition(self, condition):
        """
        Filters self items by a function that receive an item as parameter
        :param condition: A function that works as condition, receives an item as parameter and return a boolean
        :return: A self instance with items that match with condition
        """
        return Items(list(filter(condition, self.items)))

    def filter_valid(self):
        """
        Filters valid items
        :return: A self instance with valid items
        """
        return self.filter_by_condition(lambda item: item.is_valid())

    def is_valid(self):
        return self._is_valid_by_validate(InvalidItemAttribute)

    def validate(self):
        for item in self.items:
            item.validate()

    def is_empty(self):
        return self.items == []
