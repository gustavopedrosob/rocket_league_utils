from __future__ import annotations

from rl_data_utils.item.attribute_data.attribute_data import AttributesData, AttributesCollectionManagement
from rl_data_utils.item.blueprint.blueprint import Blueprint
from rl_data_utils.item.color.color import Color
from rl_data_utils.item.crafting_cost.crafting_cost import CraftingCost
from rl_data_utils.item.platform.platform import Platform
from rl_data_utils.item.price.price import Price


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
