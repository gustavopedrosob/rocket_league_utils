from __future__ import annotations

from typing import Type, Union, List

from rl_data_utils.item.attribute.has_attribute import AnyAttribute, AttributeCollection
from rl_data_utils.item.attribute.attribute import Attribute, InitializeAttribute
from rl_data_utils.item.attribute.list_attribute import ListAttribute, InitializeListAttribute
from rl_data_utils.item.attribute.regex_based_attribute import SetRegexBasedAttribute
from rl_data_utils.item.color.color import InitializeColor, Colors, Color, SetColors
from rl_data_utils.item.item.constants import FULL, AttributeName
from rl_data_utils.item.item.item import Item
from rl_data_utils.item.platform.platform import InitializePlatform, Platforms, Platform, SetPlatforms
from rl_data_utils.item.price.price import Price
from rl_data_utils.item.price.price_data import PriceData
from rl_data_utils.item.rarity.rarity import InitializeRarity, Rarities, Rarity, SetRarities
from rl_data_utils.item.serie.serie import InitializeSerie, Series, Serie, SetSeries


class DataItem(Item):
    @staticmethod
    def _auto_setter_data(
        cls: Type[Attribute],
        cls_data: Type[ListAttribute],
        value: Union[InitializeAttribute, InitializeListAttribute]
    ) -> Union[Type[Attribute], Type[ListAttribute]]:
        """
        It's used to define data properties, that can be a regular or data kind
        :param cls: Defines the regular kind
        :param cls_data: Defines the data kind
        :param value: This value defines the property
        :raise TypeError: If type of value ins't expected
        :return: A sub instance of Attribute or ListAttribute
        """
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
    def color(self) -> Union[Color, Colors]:
        return self._color

    @color.setter
    def color(self, value: Union[SetRegexBasedAttribute, SetColors]):
        self._color = self._auto_setter_data(Color, Colors, value)

    def compare_data(self, other: Union[Item, DataItem], attrs: List[AttributeName] = FULL) -> bool:
        """
        Compares two self item data with another item or item data, compares data attributes and regular attributes
        :param other: An item or data item to compare
        :param attrs: Names of attributes that you want to compare
        :raise AttributeError: If some name in attrs is invalid or the attribute is not in instance
        :raise KeyError: If mode is invalid
        :return: If both items are equals
        """
        return self.compare_data_attrs(other, self.get_attrs(attrs))

    @staticmethod
    def compare_data_attrs(other: Union[Item, DataItem], attributes: AttributeCollection) -> bool:
        """
        Compare some attributes with another DataItem or Item
        :param attributes: Attributes to compare
        :param other: An Item or ItemData to compare
        :raise TypeError: If other isn't Item or DataItem
        :return: If all both attributes match
        """
        if isinstance(DataItem, other):
            for attribute in filter(lambda a: isinstance(a, ListAttribute), attributes):
                other_attribute: AnyAttribute = getattr(other, attribute.attribute_name)
                if isinstance(other_attribute, ListAttribute):
                    if not attribute.compare(other_attribute):
                        return False
        if isinstance(Item, other):
            for attribute in filter(lambda a: isinstance(a, ListAttribute), attributes):
                other_attribute = getattr(other, attribute.attribute_name)
                if not attribute.has(other_attribute):
                    return False
                return True
        else:
            raise TypeError('Invalid type to other argument, expected Item or DataItem')

    @property
    def platform(self) -> Union[Platform, Platforms]:
        return self._platform

    @platform.setter
    def platform(self, value: Union[SetRegexBasedAttribute, SetPlatforms]):
        self._platform = self._auto_setter_data(Platform, Platforms, value)

    @property
    def rarity(self) -> Union[Rarity, Rarities]:
        return self._rarity

    @rarity.setter
    def rarity(self, value: Union[SetRegexBasedAttribute, SetRarities]):
        self._rarity = self._auto_setter_data(Rarity, Rarities, value)

    @property
    def serie(self) -> Union[Serie, Series]:
        return self._serie

    @serie.setter
    def serie(self, value: Union[SetRegexBasedAttribute, SetSeries]):
        self._serie = self._auto_setter_data(Serie, Series, value)

    @property
    def price(self) -> Union[Price, PriceData]:
        return self._price

    @price.setter
    def price(self, value: Union[Price, PriceData, None]):
        if value is None:
            self._price = Price()
        elif isinstance(value, PriceData) or isinstance(value, Price):
            self._price = value
        else:
            raise TypeError('Invalid type, Price, PriceData or None.')

    def to_item(self, serie: InitializeSerie = None, platform: InitializePlatform = None, color: InitializeColor = None,
                rarity: InitializeRarity = None) -> Item:
        """
        Transform the self DataItem into a new Item
        :param serie: A specific serie to set in this new Item
        :param platform: A specific platform to set in this new Item
        :param color: A specific color to set in this new Item
        :param rarity: A specific rarity to set in this new Item
        :return: A new Item based at itself
        """
        serie = Serie.initialize(serie)
        platform = Platform.initialize(platform)
        color = Color.initialize(color)
        rarity = Rarity.initialize(rarity)
        to_update = {a.attribute_name: a for a in [serie, platform, color, rarity] if not a.is_undefined()}
        kwargs = self.get_attr_dict()
        kwargs.update(to_update)
        return Item(**kwargs)
