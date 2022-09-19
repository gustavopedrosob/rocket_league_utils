from __future__ import annotations

from rl_data_utils.item.attribute.attribute import ItemAttribute, Archived, Blueprint, Certified, Color, Favorite, Name, \
    Platform, Price, Quantity, Rarity, Serie, Slot, Tradable
from rl_data_utils.item.attribute_data.attribute_data import AttributesData, AttributesCollectionManagement, \
    CraftingCost, Paintable
from rl_data_utils.item.attribute_string.attributes_string import AttributesString
from rl_data_utils.item.item.represents_item import RepresentsItem
from rl_data_utils.rocket_league.rocket_league import FromStr


class Item(AttributesCollectionManagement, FromStr, RepresentsItem):
    def __init__(self,
                 archived=None,
                 name=None,
                 slot=None,
                 color=None,
                 rarity=None,
                 certified=None,
                 quantity=None,
                 blueprint=None,
                 paintable=None,
                 platform=None,
                 price=None,
                 serie=None,
                 tradable=None,
                 crafting_cost=None,
                 favorite=None,
                 acquired=None) -> None:
        self.archived = archived
        self.blueprint = blueprint
        self.certified = certified
        self.color = color
        self.name = name
        self.paintable = paintable
        self.platform = platform
        self.price = price
        self.quantity = quantity
        self.rarity = rarity
        self.serie = serie
        self.slot = slot
        self.tradable = tradable
        self.crafting_cost = crafting_cost
        self.favorite = favorite
        self.acquired = acquired

    @classmethod
    def create_random(cls):
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
                   serie=Serie.create_random(),
                   favorite=Favorite.create_random())

    def is_non_crate(self, rarity):
        """
        It says if self is non crate and has some rarity
        :param rarity: A rarity to compare
        :return: If self is non crate and has some rarity
        """
        return not self.serie and self.rarity.compare(rarity)

    @classmethod
    def from_str(cls, string: str):
        """
        Creates a self instance by a string
        :param string: Any string that represents some item
        :return: An instance of Item
        """
        return cls(**AttributesString(string).get_attributes_dict())

    @staticmethod
    def match_attributes(attribute_1, attribute_2) -> bool:
        """
        It says if some attribute match with another
        :param attribute_1: Any attribute
        :param attribute_2: Any attribute
        :return: If some attribute match with another
        """
        if attribute_1 and attribute_2:
            if isinstance(attribute_1, AttributesData) and isinstance(attribute_2, ItemAttribute):
                return attribute_1.has(attribute_2)
            elif isinstance(attribute_2, AttributesData) and isinstance(attribute_1, ItemAttribute):
                return attribute_2.has(attribute_1)
            else:
                return attribute_1.compare(attribute_2)
        else:
            return False
