from __future__ import annotations

from typing import Union, Dict, Any, TypedDict, Optional

from rl_data_utils.item.archived.archived import Archived
from rl_data_utils.item.attribute_data.attribute_data import AttributesCollectionManagement
from rl_data_utils.item.blueprint.blueprint import Blueprint
from rl_data_utils.item.certified.certified import Certified, Certificates
from rl_data_utils.item.color.color import Color, Colors
from rl_data_utils.item.crafting_cost.crafting_cost import CraftingCost
from rl_data_utils.item.item.item import Item
from rl_data_utils.item.item.represents_item import RepresentsItem
from rl_data_utils.item.name.name import Name
from rl_data_utils.item.paintable.paintable import Paintable
from rl_data_utils.item.platform.platform import Platform, Platforms
from rl_data_utils.item.price.price import Price
from rl_data_utils.item.price.price_data import PriceData
from rl_data_utils.item.quantity.quantity import Quantity
from rl_data_utils.item.rarity.rarity import Rarity, Rarities
from rl_data_utils.item.serie.serie import Serie, Series
from rl_data_utils.item.slot.slot import Slot, Slots
from rl_data_utils.item.tradable.tradable import Tradable


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
                 **kwargs: Dict[str, Any]):
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
        self.unknown_arguments = kwargs

    def to_item(self,
                serie: Optional[Serie] = ...,
                platform: Optional[Platform] = ...,
                color: Optional[Color] = ...,
                rarity: Optional[Rarity] = ...) -> Item: ...

    def get_attributes_dict(self) -> DataItemDict: ...
