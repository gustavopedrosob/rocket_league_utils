from __future__ import annotations
from rl_data_utils.item import Color, Rarity, Serie, Colors, Rarities, Platforms, Series, Platform, Price
from rl_data_utils.item.attribute.attribute import Attribute
from rl_data_utils.item.attribute.list_attribute import ListAttribute
from rl_data_utils.item.item.item import Item


class DataItem(Item):
    @staticmethod
    def _auto_setter_data(cls: Attribute.__class__, cls_data: ListAttribute.__class__, value):
        if isinstance(value, cls):
            return value
        elif isinstance(value, cls_data):
            return value
        elif isinstance(value, cls.attribute_type) or value is None or value == cls.undefined_value:
            return cls(value)
        elif isinstance(value, cls_data.attribute_type) or value == cls_data.undefined_value:
            return cls_data(value)
        else:
            msg = f'Invalid type to property {cls.attribute_name}' \
                  f', expected {cls.__name__}, {cls_data.__name__}, {cls.attribute_type} or {cls_data.attribute_type}.'
            raise TypeError(msg)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = self._auto_setter_data(Color, Colors, value)

    def compare_data(self, other: Item or DataItem):
        if isinstance(DataItem, other):
            for attribute in self.get_attributes(lambda a: isinstance(a, ListAttribute)):
                other_attribute = getattr(other, attribute.attribute_name)
                if isinstance(other_attribute, ListAttribute):
                    if not attribute.compare(other_attribute):
                        return False
                elif isinstance(other_attribute, Attribute):
                    if not attribute.has(other_attribute):
                        return False
            return True
        elif isinstance(Item, other):
            for attribute in self.get_attributes(lambda a: isinstance(a, ListAttribute)):
                other_attribute = getattr(other, attribute.attribute_name)
                if not attribute.has(other_attribute):
                    return False
                return True
        else:
            raise TypeError('Invalid type to other argument, expected Item or DataItem')

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = self._auto_setter_data(Platform, Platforms, value)
    
    @property
    def rarity(self):
        return self._rarity

    @rarity.setter
    def rarity(self, value):
        self._rarity = self._auto_setter_data(Rarity, Rarities, value)

    @property
    def serie(self):
        return self._serie

    @serie.setter
    def serie(self, value):
        self._serie = self._auto_setter_data(Serie, Series, value)

    def to_item(self, serie=None, platform=None, color=None, rarity=None):
        serie = Serie.initialize(serie)
        platform = Platform.initialize(platform)
        color = Color.initialize(color)
        rarity = Rarity.initialize(rarity)
        to_update = {attribute.attribute_name: attribute
                     for attribute in [serie, platform, color, rarity] if not attribute.is_undefined()}
        kwargs = self.get_all_attributes_dict()
        kwargs.update(to_update)
        return Item(**kwargs)


