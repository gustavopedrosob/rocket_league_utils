from __future__ import annotations

from datetime import datetime
from typing import Union, TypedDict, Optional

from rl_data_utils.item.attribute.attribute import ItemAttribute, Archived, Blueprint, Certified, Color, Favorite, Name, \
    Platform, Price, Quantity, Rarity, Serie, Slot, Tradable
from rl_data_utils.item.attribute_data.attribute_data import AttributesData, AttributesCollectionManagement, \
    CraftingCost, Paintable
from rl_data_utils.item.item.represents_item import RepresentsItem
from rl_data_utils.rocket_league.rocket_league import FromStr


class ItemDict(TypedDict):
    archived: Archived
    name: Name
    slot: Slot
    color: Color
    rarity: Rarity
    certified: Certified
    quantity: Quantity
    blueprint: Blueprint
    paintable: Paintable
    platform: Platform
    price: Price
    serie: Serie
    tradable: Tradable
    crafting_cost: CraftingCost
    favorite: Favorite


class Item(AttributesCollectionManagement, FromStr, RepresentsItem):
    def __init__(self,
                 archived: Optional[Archived] = ...,
                 name: Optional[Name] = ...,
                 slot: Optional[Slot] = ...,
                 color: Optional[Color] = ...,
                 rarity: Optional[Rarity] = ...,
                 certified: Optional[Certified] = ...,
                 quantity: Optional[Quantity] = ...,
                 blueprint: Optional[Blueprint] = ...,
                 paintable: Optional[Paintable] = ...,
                 platform: Optional[Platform] = ...,
                 price: Optional[Price] = ...,
                 serie: Optional[Serie] = ...,
                 tradable: Optional[Tradable] = ...,
                 crafting_cost: Optional[CraftingCost] = ...,
                 favorite: Optional[Favorite] = ...,
                 acquired: Optional[datetime] = ...) -> None:
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
        self.acquired = acquired

    def get_attributes_dict(self) -> ItemDict: ...

    @classmethod
    def create_random(cls) -> Item: ...

    def is_non_crate(self, rarity: Rarity) -> bool: ...

    @classmethod
    def create_undefined(cls) -> Item: ...

    @classmethod
    def from_str(cls, string: str) -> Item: ...

    @staticmethod
    def match_attributes(attribute_1: Optional[Union[ItemAttribute, AttributesData]],
                         attribute_2: Optional[Union[ItemAttribute, AttributesData]]) -> bool: ...
