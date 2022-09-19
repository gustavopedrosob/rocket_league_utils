from __future__ import annotations

from typing import Union, TypedDict, Optional

from rl_data_utils.item.attribute.attribute import Archived, Blueprint, Certified, Color, Favorite, Name, Platform, \
    Price, Quantity, Rarity, Serie, Slot, Tradable
from rl_data_utils.item.attribute_data.attribute_data import AttributesCollectionManagement, CraftingCost, Paintable, \
    PriceData, Series, Slots, Certificates, Colors, Platforms, Rarities
from rl_data_utils.item.item.item import Item
from rl_data_utils.item.item.represents_item import RepresentsItem


class DataItemDict(TypedDict):
    archived: Archived
    name: Name
    slot: Union[Slot, Slots]
    color: Union[Color, Colors]
    rarity: Union[Rarity, Rarities]
    certified: Union[Certified, Certificates]
    quantity: Quantity
    blueprint: Blueprint
    paintable: Paintable
    platform: Union[Platform, Platforms]
    price: Union[Price, PriceData]
    serie: Union[Serie, Series]
    tradable: Tradable
    crafting_cost: CraftingCost
    favorite: Favorite



class DataItem(RepresentsItem, AttributesCollectionManagement):
    def __init__(self,
                 archived: Optional[Archived] = ...,
                 name: Optional[Name] = ...,
                 slot: Optional[Union[Slot, Slots]] = ...,
                 color: Optional[Union[Color, Colors]] = ...,
                 rarity: Optional[Union[Rarity, Rarities]] = ...,
                 certified: Optional[Union[Certified, Certificates]] = ...,
                 quantity: Optional[Quantity] = ...,
                 blueprint: Optional[Blueprint] = ...,
                 paintable: Optional[Paintable] = ...,
                 platform: Optional[Union[Platform, Platforms]] = ...,
                 price: Optional[Union[Price, PriceData]] = ...,
                 serie: Optional[Union[Serie, Series]] = ...,
                 tradable: Optional[Tradable] = ...,
                 crafting_cost: Optional[CraftingCost] = ...,
                 favorite: Optional[Favorite] = ...):
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

    def to_item(self,
                serie: Optional[Serie] = ...,
                platform: Optional[Platform] = ...,
                color: Optional[Color] = ...,
                rarity: Optional[Rarity] = ...) -> Item: ...

    def get_attributes_dict(self) -> DataItemDict: ...
