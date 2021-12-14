from __future__ import annotations

from typing import Union, Callable, List, Literal

from rl_data_utils.exceptions import AttributeNotExists
from rl_data_utils.item.attribute.any_attribute import AnyAllAttribute
from rl_data_utils.item.attribute_collections.attribute_collections import AttributeCollection
from rl_data_utils.item.item.constants import Modes, FULL
from rl_data_utils.item.item.item import Item, InitializeItem

SetItems = Union[List[InitializeItem], None]

AttributesNames = Literal['archived', 'blueprint', 'certified', 'color', 'name', 'paintable', 'platform', 'price',
                          'quantity', 'rarity', 'serie', 'slot', 'tradable']


class Items:
    def __init__(self, items: InitializeItems = None):
        self.items: List[Item] = items

    def __repr__(self) -> str:
        return ', '.join([repr(item) for item in self.items])

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

    def filter_by_item(self, item: InitializeItem, mode: Modes = FULL):
        """
        Filters self items by an Item, it ignores undefined attributes to filter
        :param item: A item to find in items
        :param mode: If mode is indenfitier then it will compare just indentifier attributes or if it's full then it
        will compare all attributes from both
        :raise KeyError: If mode is Invalid
        :return A self instance with items that match with item
        """
        item = Item.initialize(item)
        modes = {'indentifier': item.get_indentifier_attrs, 'full': item.get_item_attrs}
        attributes: AttributeCollection = modes[mode]()
        attributes.filter(lambda attr: not attr.is_undefined())
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
        return self.filter_by_attribute_condition(attribute.attribute_name, lambda attr: attr.compare(attribute))

    def filter_by_attribute_condition(self,
                                      attr_name: AttributesNames,
                                      condition: Callable[[AnyAllAttribute], bool]) -> Items:
        """
        Filters self items by a function that receive an attribute as parameter
        :param attr_name: A attribute name
        :param condition: A function that works as condition, receives an attribute as parameter and return a boolean
        :raise AttributeError: If attr_name doesn't exist
        :return: A self instance with items that match with condition
        """
        return self.filter_by_condition(lambda item: condition(getattr(item, attr_name)))

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
