from __future__ import annotations

from typing import Optional

from rl_data_utils.item.attribute_data.attribute_data import AttributesData, AttributesCollectionManagement
from rl_data_utils.item.blueprint.blueprint import Blueprint
from rl_data_utils.item.color.color import Color
from rl_data_utils.item.crafting_cost.crafting_cost import CraftingCost
from rl_data_utils.item.platform.platform import Platform
from rl_data_utils.item.price.price import Price


class DataPrice(AttributesCollectionManagement, AttributesData):
    def __init__(self,
                 color: Optional[Color] = ...,
                 platform: Optional[Platform] = ...,
                 crafting_cost: Optional[CraftingCost] = ...,
                 price: Optional[Price] = ...,
                 blueprint: Optional[Blueprint] = ...) -> None:
        self.color = color
        self.platform = platform
        self.crafting_cost = crafting_cost
        self.price = price
        self.blueprint = blueprint
        super().__init__()

    @classmethod
    def create_random(cls) -> DataPrice: ...
