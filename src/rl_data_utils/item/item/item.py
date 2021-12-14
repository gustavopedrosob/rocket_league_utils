from __future__ import annotations

from typing import Union, Dict, Any

from rl_data_utils.exceptions import RlAttributeError
from rl_data_utils.item.archived.archived import Archived, InitializeArchived
from rl_data_utils.item.attribute.any_attribute import AnyAttribute
from rl_data_utils.item.attribute.bool_attribute import SetBoolAttribute
from rl_data_utils.item.attribute.int_attribute import SetIntAttribute
from rl_data_utils.item.attribute.list_attribute import ListAttribute
from rl_data_utils.item.attribute.regex_based_attribute import SetRegexBasedAttribute
from rl_data_utils.item.attribute.str_attribute import StrAttribute, SetStrAttribute
from rl_data_utils.item.attribute_collections.attribute_collections import AttributeCollection
from rl_data_utils.item.attribute_string.attributes_string import AttributesString, InitializeAttributesString
from rl_data_utils.item.blueprint.blueprint import InitializeBlueprint, Blueprint
from rl_data_utils.item.certified.certified import InitializeCertified, Certified
from rl_data_utils.item.color.color import InitializeColor, Color
from rl_data_utils.item.item.constants import FULL, Modes
from rl_data_utils.item.name.name import InitializeName, Name
from rl_data_utils.item.paintable.paintable import InitializePaintable, Paintable
from rl_data_utils.item.platform.platform import InitializePlatform, Platform
from rl_data_utils.item.price.price import InitializePrice, Price
from rl_data_utils.item.quantity.quantity import InitializeQuantity, Quantity
from rl_data_utils.item.rarity.constants import VERY_RARE, IMPORT, EXOTIC, RARE
from rl_data_utils.item.rarity.rarity import InitializeRarity, Rarity
from rl_data_utils.item.serie.serie import InitializeSerie, Serie
from rl_data_utils.item.slot.slot import InitializeSlot, Slot
from rl_data_utils.item.tradable.tradable import InitializeTradable, Tradable


class Item:
    def __init__(self,
                 archived: InitializeArchived = None,
                 name: InitializeName = None,
                 slot: InitializeSlot = None,
                 color: InitializeColor = None,
                 rarity: InitializeRarity = None,
                 certified: InitializeCertified = None,
                 quantity: InitializeQuantity = None,
                 blueprint: InitializeBlueprint = None,
                 paintable: InitializePaintable = None,
                 platform: InitializePlatform = None,
                 price: InitializePrice = None,
                 serie: InitializeSerie = None,
                 tradable: InitializeTradable = None,
                 **kwargs: dict):
        self.archived: Archived = archived
        self.blueprint: Blueprint = blueprint
        self.certified: Certified = certified
        self.color: Color = color
        self.name: Name = name
        self.paintable: Paintable = paintable
        self.platform: Platform = platform
        self.price: Price = price
        self.quantity: Quantity = quantity
        self.rarity: Rarity = rarity
        self.serie: Serie = serie
        self.slot: Slot = slot
        self.tradable: Tradable = tradable
        self.unknown_arguments: dict = kwargs

    def __eq__(self, other: Item) -> bool:
        return self.compare(other)

    def __repr__(self) -> str:
        attributes = self.get_all_attrs().filter(
            lambda attribute: not attribute.is_undefined() and attribute.is_valid()).attributes
        attributes.sort(key=lambda attr: attr.order)
        attributes_string = ', '.join([repr(attr) for attr in attributes])
        return f'{self.__class__.__name__}({attributes_string})'

    @property
    def archived(self) -> Archived:
        return self._archived

    @archived.setter
    def archived(self, value: SetBoolAttribute):
        self._archived = Archived.initialize(value)

    @property
    def blueprint(self) -> Blueprint:
        return self._blueprint

    @blueprint.setter
    def blueprint(self, value: SetBoolAttribute):
        self._blueprint = Blueprint.initialize(value)

    @property
    def certified(self) -> Certified:
        return self._certified

    @certified.setter
    def certified(self, value: SetRegexBasedAttribute):
        self._certified = Certified.initialize(value)

    @property
    def color(self) -> Color:
        return self._color

    @color.setter
    def color(self, value: SetRegexBasedAttribute):
        self._color = Color.initialize(value)

    def compare(self, item: InitializeItem, mode: Modes = FULL) -> bool:
        """
        Compares two items depending on the mode
        :param item: An item to compare
        :param mode: If mode is indenfitier then it will compare just indentifier attributes or if it's full then it
        will compare all attributes from both
        :raise KeyError: If mode is invalid
        :return: If both items are equals
        """
        modes = {"indentifier": self.get_indentifier_attrs, "full": self.get_item_attrs}
        return self.compare_attrs(item, modes[mode]())

    def get_item_attrs(self) -> AttributeCollection:
        return self.get_all_attrs().filter(lambda attribute: not isinstance(attribute, ListAttribute))

    @staticmethod
    def compare_attrs(item: InitializeItem, attributes: AttributeCollection) -> bool:
        """
        Compare some attributes with another item
        :param item: Another item to compare
        :param attributes: Attributes to compare
        :return: If all both attributes match
        """
        item = Item.initialize(item)
        for attribute in attributes:
            other_attribute = getattr(item, attribute.attribute_name)
            if isinstance(other_attribute, StrAttribute):
                if not attribute.compare(other_attribute):
                    return False
            elif isinstance(other_attribute, ListAttribute):
                if not other_attribute.has(attribute):
                    return False
        return True

    @staticmethod
    def from_attribute_string(attributes_string: InitializeAttributesString) -> Item:
        """
        Creates an Item using AttributesString or a simple string
        :param attributes_string: str or AttributesString that represents an item
        :return: An Item from string
        """
        attributes_string = AttributesString.initialize_string(attributes_string)
        return Item(**attributes_string.get_attributes_dict())

    @classmethod
    def create_random(cls) -> Item:
        """
        Creates an items with all random attributes
        :return: An item with random attributes
        """
        return cls(archived=Archived.create_random(),
                   name=Name.create_random(),
                   slot=Slot.create_random(),
                   color=Color.create_random(),
                   rarity=Rarity.create_random(),
                   certified=Certified.create_random(),
                   quantity=Quantity.create_random(),
                   blueprint=Blueprint.create_random(),
                   paintable=Paintable.create_random(),
                   platform=Platform.create_random(),
                   price=Price.create_random(),
                   tradable=Tradable.create_random())

    def get_all_attrs(self) -> AttributeCollection:
        """
        Gets all attributes
        :return: All attributes
        """
        return AttributeCollection([
            self.archived, self.name, self.color, self.slot, self.rarity, self.certified, self.quantity, self.blueprint,
            self.paintable, self.platform, self.price, self.serie, self.tradable])

    def get_indentifier_attrs(self) -> AttributeCollection:
        return AttributeCollection([self.name, self.rarity, self.slot, self.blueprint, self.platform])

    def get_all_attrs_dict(self) -> Dict[str, AnyAttribute]:
        """
        Get all attributes with their respective names
        :return: A dict of attributes
        """
        return {attribute.attribute_name: attribute for attribute in self.get_all_attrs()}

    @classmethod
    def initialize(cls, value: InitializeItem) -> Item:
        if isinstance(value, Item):
            return value
        elif isinstance(value, dict):
            return Item(**value)
        elif isinstance(value, str) or isinstance(value, AttributesString):
            return cls.from_attribute_string(value)
        else:
            raise TypeError('Invalid type, expected Item, dict, str or AttributesString.')

    def is_undefined(self) -> bool:
        """
        Says if all attributes are undefined
        :return: If all attributes are undefined
        """
        for attribute in self.get_all_attrs():
            if not attribute.is_undefined():
                return False
        return True

    def is_ncr(self) -> bool:
        return self.serie.is_undefined() and self.rarity.is_exactly(RARE)

    def is_ncvr(self) -> bool:
        return self.serie.is_undefined() and self.rarity.is_exactly(VERY_RARE)

    def is_nci(self) -> bool:
        return self.serie.is_undefined() and self.rarity.is_exactly(IMPORT)

    def is_nce(self) -> bool:
        return self.serie.is_undefined() and self.rarity.is_exactly(EXOTIC)

    def is_valid(self) -> bool:
        """
        Says if it's valid
        :return: If it's valid
        """
        try:
            self.validate()
        except RlAttributeError:
            return False
        else:
            return True

    @property
    def name(self) -> Name:
        return self._name

    @name.setter
    def name(self, value: SetStrAttribute):
        self._name = Name.initialize(value)

    @property
    def paintable(self) -> Paintable:
        return self._paintable

    @paintable.setter
    def paintable(self, value: SetBoolAttribute):
        self._paintable = Paintable.initialize(value)

    @property
    def platform(self) -> Platform:
        return self._platform

    @platform.setter
    def platform(self, value: SetRegexBasedAttribute):
        self._platform = Platform.initialize(value)

    @property
    def price(self) -> Price:
        return self._price

    @price.setter
    def price(self, value):
        self._price = Price.initialize(value)

    @property
    def quantity(self) -> Quantity:
        return self._quantity

    @quantity.setter
    def quantity(self, value: SetIntAttribute):
        self._quantity = Quantity.initialize(value)

    @property
    def rarity(self) -> Rarity:
        return self._rarity

    @rarity.setter
    def rarity(self, value: SetRegexBasedAttribute):
        self._rarity = Rarity.initialize(value)

    @property
    def serie(self) -> Serie:
        return self._serie

    @serie.setter
    def serie(self, value: SetRegexBasedAttribute):
        self._serie = Serie.initialize(value)

    @property
    def slot(self) -> Slot:
        return self._slot

    @slot.setter
    def slot(self, value: SetRegexBasedAttribute):
        self._slot = Slot.initialize(value)

    @property
    def tradable(self) -> Tradable:
        return self._tradable

    @tradable.setter
    def tradable(self, value: SetBoolAttribute):
        self._tradable = Tradable.initialize(value)

    def validate(self):
        """
        Validates all attributes
        :raise AttributeNotExists: If any RegexBasedAttribute attribute is invalid
        """
        for attribute in self.get_all_attrs():
            attribute.validate()


InitializeItem = Union[Item, Dict[str, Any], str, AttributesString]
