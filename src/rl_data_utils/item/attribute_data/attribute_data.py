from __future__ import annotations

from abc import abstractmethod, ABCMeta

from rl_data_utils.exceptions import InvalidItemAttribute
from rl_data_utils.item.attribute.attribute import ItemAttribute, Color, Platform, Price, Blueprint, PriceInfo, \
    CreditsQuantity, SerieInfo, Serie, SlotInfo, Slot, BoolItemAttribute, AttributeInfo, CertifiedInfo, ColorInfo, \
    PlatformInfo, RarityInfo, Rarity, Certified, StaticItemAttribute
from rl_data_utils.item.item.constants import CRAFTING_COST, PAINTABLE
from rl_data_utils.rocket_league.rocket_league import RocketLeagueObject, Validable, Comparable, CanBeEmpty, Contains, \
    Identifiable, FromStrList


class HasAttributes(Validable, Comparable, CanBeEmpty, Contains):
    @abstractmethod
    def get_attributes(self):
        pass

    def is_empty(self):
        return len(self.get_attributes()) == 0

    def is_valid(self):
        return self._is_valid_by_validate(InvalidItemAttribute)

    def validate(self):
        for attr in self.get_attributes():
            if isinstance(attr, Validable):
                attr.validate()


class AttributesData(RocketLeagueObject, HasAttributes, Identifiable, metaclass=ABCMeta):
    pass


class AttributesManagement(HasAttributes):
    def __init__(self, attributes):
        self.attributes = attributes

    def compare(self, other, condition=None) -> bool:
        if condition:
            return all(other.has(attr) for attr in self.attributes if condition(attr))
        else:
            return all(other.has(attr) for attr in self.attributes)

    def get_attributes(self):
        return self.attributes

    def get_respective(self, other):
        for attr in self.attributes:
            if other.compare(attr):
                return attr
        return None

    def has(self, attribute) -> bool:
        return any(attr.compare(attribute) for attr in self.attributes)


class AttributesCollectionManagement(HasAttributes):
    def compare(self, other, condition=None):
        if self.is_empty():
            return False
        elif condition:
            return all(getattr(other, k).compare(attr)
                       for k, attr in self.get_attributes_dict().items() if condition(attr))
        else:
            return all(getattr(other, k).compare(attr) for k, attr in self.get_attributes_dict().items())

    def get_attributes(self):
        return tuple(self.get_attributes_dict().values())

    def get_attributes_dict(self):
        return {k: v for k, v in self.__dict__.items()
                if v and (isinstance(v, ItemAttribute) or isinstance(v, AttributesData))}

    def has(self, attribute):
        our_attr = getattr(self, attribute.identifier)
        return attribute.compare(our_attr)


class CraftingCostInfo(AttributeInfo):
    identifier = CRAFTING_COST


class CraftingCost(CreditsQuantity):
    pass


class PaintableInfo(AttributeInfo):
    identifier = PAINTABLE
    order = 10


class Paintable(BoolItemAttribute, PaintableInfo):
    pass


class DataPrice(AttributesCollectionManagement, AttributesData):
    def __init__(self,
                 color=None,
                 platform=None,
                 crafting_cost=None,
                 price=None,
                 blueprint=None):
        self.color: Color = color
        self.platform: Platform = platform
        self.crafting_cost: CraftingCost = crafting_cost
        self.price: Price = price
        self.blueprint: Blueprint = blueprint
        super().__init__()

    @classmethod
    def create_random(cls):
        return DataPrice(color=Color.create_random(),
                         platform=Platform.create_random(),
                         crafting_cost=CraftingCost.create_random(),
                         price=Price.create_random(),
                         blueprint=Blueprint.create_random())


class PriceData(AttributesData, PriceInfo, AttributesManagement):
    sub_attribute = DataPrice

    def __init__(self, prices):
        self.prices = prices
        super().__init__(self.prices)

    def get_price(self,
                  color=None,
                  platform=None,
                  blueprint=None):
        data_prices = self.prices
        for attr in filter(lambda t: bool(t), (color, platform, blueprint)):
            data_prices = list(filter(
                lambda dp: attr.compare(getattr(dp, attr.identifier)), data_prices))
        data_price = data_prices[0]
        return data_price.price, data_price.crafting_cost


class RegexBasedListAttribute(AttributesData, FromStrList, AttributesManagement):
    attribute_class = None

    @classmethod
    def from_str_list(cls, str_list):
        return cls(list(map(lambda str_: cls.attribute_class(str_), str_list)))


class Series(RegexBasedListAttribute, SerieInfo):
    attribute_class = Serie


class Slots(RegexBasedListAttribute, SlotInfo):
    attribute_class = Slot


class Certificates(RegexBasedListAttribute, CertifiedInfo):
    attribute_class = Certified


class Colors(RegexBasedListAttribute, ColorInfo):
    attribute_class = Color


class Platforms(RegexBasedListAttribute, PlatformInfo):
    attribute_class = Platform


class Rarities(RegexBasedListAttribute, RarityInfo):
    attribute_class = Rarity


class StaticAttributeData(AttributesManagement, AttributesData):
    pass
