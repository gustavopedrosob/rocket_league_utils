from __future__ import annotations

from typing import Union

from rl_data_utils.item.attribute.has_attribute import HasAttribute
from rl_data_utils.item.blueprint.blueprint import InitializeBlueprint, Blueprint, HasBlueprint
from rl_data_utils.item.color.color import InitializeColor, Color, HasColor
from rl_data_utils.item.platform.platform import InitializePlatform, Platform, HasPlatform
from rl_data_utils.item.crafting_cost.crafting_cost import CraftingCost, InitializeCraftingCost, HasCraftingCost
from rl_data_utils.item.price.price import InitializePrice, Price, HasPrice


class DataPrice(HasAttribute, HasColor, HasPlatform, HasBlueprint, HasCraftingCost, HasPrice):
    def __init__(self,
                 color: InitializeColor = None,
                 platform: InitializePlatform = None,
                 crafting_cost: InitializeCraftingCost = None,
                 price: InitializePrice = None,
                 blueprint: InitializeBlueprint = None):
        super(DataPrice, self).__init__()
        self.color: Color = color
        self.platform: Platform = platform
        self.crafting_cost: CraftingCost = crafting_cost
        self.price: Price = price
        self.blueprint: Blueprint = blueprint

    def __repr__(self) -> str:
        return 'DataPrice({})'.format(self.get_attrs())

    def compare(self, other: DataPrice) -> bool:
        return all(attr.compare(other.get_attr(attr.attribute)) for attr in self.get_attrs(ignore_undefined=True))

    @classmethod
    def initialize(cls, value: Union[DataPrice, dict, None]) -> DataPrice:
        if value is None:
            return cls()
        if isinstance(value, cls):
            return value
        elif isinstance(value, dict):
            return cls(**value)
        else:
            raise TypeError('Invalid type, expected DataPrice, dict or None.')
