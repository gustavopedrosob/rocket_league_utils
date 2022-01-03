from __future__ import annotations

from datetime import datetime
from typing import Union, TypedDict, Optional

from rl_data_utils.item.archived.archived import Archived
from rl_data_utils.item.attribute.attribute import ItemAttribute
from rl_data_utils.item.attribute_data.attribute_data import AttributesData, AttributesCollectionManagement
from rl_data_utils.item.blueprint.blueprint import Blueprint
from rl_data_utils.item.certified.certified import Certified
from rl_data_utils.item.color.color import Color
from rl_data_utils.item.crafting_cost.crafting_cost import CraftingCost
from rl_data_utils.item.favorite.favorite import Favorite
from rl_data_utils.item.item.represents_item import RepresentsItem
from rl_data_utils.item.name.name import Name
from rl_data_utils.item.paintable.paintable import Paintable
from rl_data_utils.item.platform.platform import Platform
from rl_data_utils.item.price.price import Price
from rl_data_utils.item.quantity.quantity import Quantity
from rl_data_utils.item.rarity.rarity import Rarity
from rl_data_utils.item.serie.serie import Serie
from rl_data_utils.item.slot.slot import Slot
from rl_data_utils.item.tradable.tradable import Tradable
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
