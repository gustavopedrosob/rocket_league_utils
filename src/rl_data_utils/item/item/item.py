from __future__ import annotations

from typing import Union, Dict, Any, List

from rl_data_utils.item.archived.archived import Archived, InitializeArchived, HasArchived
from rl_data_utils.item.attribute.has_attribute import HasAttribute, AttributeCollection
from rl_data_utils.item.attribute.list_attribute import ListAttribute
from rl_data_utils.item.attribute.str_attribute import StrAttribute
from rl_data_utils.item.attribute_string.attributes_string import AttributesString, InitializeAttributesString
from rl_data_utils.item.blueprint.blueprint import InitializeBlueprint, Blueprint, HasBlueprint
from rl_data_utils.item.certified.certified import InitializeCertified, Certified, HasCertified
from rl_data_utils.item.color.color import InitializeColor, Color, HasColor
from rl_data_utils.item.crafting_cost.crafting_cost import InitializeCraftingCost, CraftingCost, HasCraftingCost
from rl_data_utils.item.item.constants import FULL, AttributeName
from rl_data_utils.item.name.name import InitializeName, Name, HasName
from rl_data_utils.item.paintable.paintable import InitializePaintable, Paintable, HasPaintable
from rl_data_utils.item.platform.platform import InitializePlatform, Platform, HasPlatform
from rl_data_utils.item.price.price import InitializePrice, Price, HasPrice
from rl_data_utils.item.quantity.quantity import InitializeQuantity, Quantity, HasQuantity
from rl_data_utils.item.rarity.constants import VERY_RARE, IMPORT, EXOTIC, RARE
from rl_data_utils.item.rarity.rarity import InitializeRarity, Rarity, HasRarity
from rl_data_utils.item.serie.serie import InitializeSerie, Serie, HasSerie
from rl_data_utils.item.slot.slot import InitializeSlot, Slot, HasSlot
from rl_data_utils.item.tradable.tradable import InitializeTradable, Tradable, HasTradable


class Item(HasAttribute, HasArchived, HasName, HasSlot, HasColor, HasRarity, HasCertified, HasQuantity, HasBlueprint,
           HasPaintable, HasPlatform, HasPrice, HasSerie, HasTradable, HasCraftingCost):
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
                 crafting_cost: InitializeCraftingCost = None,
                 **kwargs: dict):
        super(Item, self).__init__()
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
        self.crafting_cost: CraftingCost = crafting_cost
        self.unknown_arguments: dict = kwargs

    def __eq__(self, other: Item) -> bool:
        return self.compare(other)

    def __repr__(self) -> str:
        attributes = self.get_sorted_attrs(ignore_undefined=True)
        attributes_string = ', '.join([repr(attr) for attr in attributes])
        return f'{self.__class__.__name__}({attributes_string})'

    def get_row_repr(self) -> str:
        """
        Gets an item row representation, (It's used for create an item table representation).
        :return: An item row representation
        """
        return '|'.join([f'{attr.get_repr(maxsize=15):^15}' for attr in self.get_attrs()])

    def compare(self, item: InitializeItem, attrs: List[AttributeName] = FULL) -> bool:
        """
        Compares two items depending on the mode
        :param item: An item to compare
        :param attrs: Names of attributes that you want to compare
        :raise AttributeError: If some name in attrs is invalid or the attribute is not in instance
        :raise KeyError: If mode is invalid
        :return: If both items are equals
        """
        return self.compare_attrs(item, self.get_attrs(attrs, True))

    def get_item_attrs(self) -> AttributeCollection:
        return filter(lambda attribute: not isinstance(attribute, ListAttribute), self.get_attrs())

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
                   tradable=Tradable.create_random(),
                   crafting_cost=CraftingCost.create_random(),
                   serie=Serie.create_random())

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

    def is_ncr(self) -> bool:
        return self.serie.is_undefined() and self.rarity.is_exactly(RARE)

    def is_ncvr(self) -> bool:
        return self.serie.is_undefined() and self.rarity.is_exactly(VERY_RARE)

    def is_nci(self) -> bool:
        return self.serie.is_undefined() and self.rarity.is_exactly(IMPORT)

    def is_nce(self) -> bool:
        return self.serie.is_undefined() and self.rarity.is_exactly(EXOTIC)


InitializeItem = Union[Item, Dict[str, Any], str, AttributesString]
