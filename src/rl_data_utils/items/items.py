from __future__ import annotations

from typing import Union, Callable, List

from rl_data_utils.exceptions import AttributeNotExists
from rl_data_utils.item.attribute.has_attribute import AnyAllAttribute, AttributeCollection
from rl_data_utils.item.item.constants import FULL, AttributeName
from rl_data_utils.item.item.item import Item, InitializeItem

SetItems = Union[List[InitializeItem], None]


class Items:
    def __init__(self, items: InitializeItems = None):
        self.items: List[Item] = items

    def __repr__(self) -> str:
        return ', '.join([repr(item) for item in self.items])

    def get_table_repr(self) -> str:
        """
        Gets an item table representation like an Excel sheet as str.
        :return: An item table representation
        """
        title = '|'.join([f'{name:^15}' for name in FULL])
        contents = [item.get_row_repr() for item in self.items]
        return '\n'.join([title, *contents])

    def __iter__(self):
        for item in self.items:
            yield item

    def _auto_setter(self, value: SetItems) -> List[Item]:
        """
        It's used to set self items
        :param value: A list or None
        :return: a list of Items
        """
        if value is None or value == []:
            return []
        elif isinstance(value, list):
            value = value.copy()
            for index, v in enumerate(value):
                value[index] = Item.initialize(v)
            return value
        else:
            raise TypeError('Invalid type, expected a list.')

    def filter_by_item(self, item: InitializeItem, attrs: List[AttributeName] = FULL):
        """
        Filters self items by an Item, it ignores undefined attributes to filter
        :param item: A item to find in items
        :param attrs: Names of attributes that you want to compare
        :raise AttributeError: If some name in attrs is invalid or the attribute is not in instance
        :raise KeyError: If mode is Invalid
        :return A self instance with items that match with item
        """
        item = Item.initialize(item)
        attributes: AttributeCollection = item.get_attrs(attrs)
        attributes = filter(lambda attr: not attr.is_undefined(), attributes)
        return self.filter_by_attributes(attributes)

    def filter_by_attributes(self, attributes: AttributeCollection) -> Items:
        """
        Filters self items by attributes
        :param attributes: Attributes to compare
        :return: A self instance with items that match with attributes
        """
        items = self
        for attribute in attributes:
            items = items.filter_by_attribute(attribute)
        return items

    def filter_by_attribute(self, attribute: AnyAllAttribute) -> Items:
        """
        Filters self items by an attribute
        :param attribute: A attribute to find in items
        :return: A self instance with items that match with attribute
        """
        return self.filter_by_condition(lambda item: getattr(item, attribute.attribute_name).compare(attribute))

    def filter_by_condition(self, condition: Callable[[Item], bool]) -> Items:
        """
        Filters self items by a function that receive an item as parameter
        :param condition: A function that works as condition, receives an item as parameter and return a boolean
        :return: A self instance with items that match with condition
        """
        return Items(list(filter(condition, self.items)))

    def filter_valid(self) -> Items:
        """
        Filters valid items
        :return: A self instance with valid items
        """
        return self.filter_by_condition(lambda item: item.is_valid())

    @classmethod
    def initialize(cls, value: InitializeItems) -> Items:
        """
        Creates an instance of class using a value that can be a list or Items
        :param value: A instance of list or Items
        :return: An instance of class
        """
        if isinstance(value, list):
            return cls(value)
        elif isinstance(value, cls):
            return value
        else:
            raise TypeError('Invalid type, expected Items or list[Items].')

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value: SetItems):
        self._items = self._auto_setter(value)

    def validate(self):
        """
        Validates all items
        """
        for item in self.items:
            item.validate()

    def is_valid(self) -> bool:
        """
        Says if it's valid
        :return: If it's valid
        """
        try:
            self.validate()
        except AttributeNotExists:
            return False
        else:
            return True

    def is_undefined(self) -> bool:
        """
        Says if it's undefined
        :return: If it's undefined
        """
        return self._items == []


InitializeItems = Union[Items, SetItems]
