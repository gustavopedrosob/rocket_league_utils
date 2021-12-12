from __future__ import annotations

from typing import Type, Union, List, Dict, Callable

from rl_data_utils.item.attribute.attribute import Attribute, InitializeAttribute
from rl_data_utils.item.attribute.list_attribute import ListAttribute, InitializeListAttribute
from rl_data_utils.item.attribute.regex_based_attribute import SetRegexBasedAttribute
from rl_data_utils.item.color.color import InitializeColor, Colors, Color, SetColors
from rl_data_utils.item.item.item import Item, AnyAttribute
from rl_data_utils.item.platform.platform import InitializePlatform, Platforms, Platform, SetPlatforms
from rl_data_utils.item.rarity.rarity import InitializeRarity, Rarities, Rarity, SetRarities
from rl_data_utils.item.serie.serie import InitializeSerie, Series, Serie, SetSeries

AnyDataAttribute = Union[Colors, Rarities, Platforms, Series]
AnyAllAttribute = Union[AnyAttribute, AnyDataAttribute]


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

    def compare_data(self, other: Union[Item, DataItem]) -> bool:
        """
        Compare self with another DataItem or Item, compare their intersection Attributes
        :param other: An Item or ItemData
        :raise TypeError: If other isn't Item or DataItem
        :return: If both are equal
        """
        if isinstance(DataItem, other):
            for attribute in self.get_attributes(lambda a: isinstance(a, ListAttribute)):
                other_attribute: AnyAttribute = getattr(other, attribute.attribute_name)
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

    def get_all_attributes(self) -> List[AnyAllAttribute]:
        return super().get_all_attributes()

    def get_all_attributes_dict(self) -> Dict[str, AnyAllAttribute]:
        return super().get_all_attributes_dict()

    def get_attributes(self, condition: Callable[[Type[Attribute]], bool]) -> List[AnyAllAttribute]:
        return super().get_attributes(condition)

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
        kwargs = self.get_all_attributes_dict()
        kwargs.update(to_update)
        return Item(**kwargs)
