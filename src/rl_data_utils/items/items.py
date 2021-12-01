from __future__ import annotations

from rl_data_utils.exceptions import AttributeNotExists
from rl_data_utils.item.attribute.attribute import Attribute
from rl_data_utils.item.attribute.list_attribute import ListAttribute
from rl_data_utils.item.item.item import Item


class Items:
    def __init__(self, items=None):
        self.items = items

    def __repr__(self):
        return ', '.join([repr(item) for item in self.items])

    def __iter__(self):
        for item in self.items:
            yield item

    def _auto_setter(self, value):
        if value is None or value == []:
            return []
        elif isinstance(value, list):
            for index, v in enumerate(value):
                value[index] = Item.initialize(v)
            return value
        else:
            raise TypeError('Invalid type, expected a list.')

    def filter_by(self, item: Item or dict or str) -> Items:
        item = Item.initialize(item)
        items = self
        for attribute in item.get_attributes(lambda a: not isinstance(a, ListAttribute) and not a.is_undefined()):
            items = items.filter_by_attribute(attribute)
        return items

    def filter_by_attribute(self, attribute: Attribute) -> Items:
        return self.filter_by_attribute_condition(attribute.attribute_name, lambda attr: attr.compare(attribute))

    def filter_by_attribute_condition(self, attr_name, expression):
        return self.filter_by_condition(lambda item: expression(getattr(item, attr_name)))

    def filter_by_condition(self, lamb) -> Items:
        return Items(list(filter(lamb, self.items)))

    def filter_valid(self) -> Items:
        return self.filter_by_condition(lambda item: item.is_valid())

    @classmethod
    def initialize(cls, value):
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
    def items(self, value):
        self._items = self._auto_setter(value)

    def validate(self):
        for item in self.items:
            item.validate()

    def is_valid(self):
        try:
            self.validate()
        except AttributeNotExists:
            return False
        else:
            return True

    def is_undefined(self):
        return self._items == []
