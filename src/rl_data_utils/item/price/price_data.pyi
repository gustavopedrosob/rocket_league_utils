from typing import List, Tuple, Optional

from rl_data_utils.item.attribute_data.attribute_data import AttributesData, AttributesManagement
from rl_data_utils.item.blueprint.blueprint import Blueprint
from rl_data_utils.item.color.color import Color
from rl_data_utils.item.crafting_cost.crafting_cost import CraftingCost
from rl_data_utils.item.platform.platform import Platform
from rl_data_utils.item.price.data_price import DataPrice
from rl_data_utils.item.price.price import PriceInfo, Price


class PriceData(AttributesData, PriceInfo, AttributesManagement[DataPrice]):
    sub_attribute = DataPrice

    def __init__(self, prices: List[DataPrice]) -> None:
        self.prices = prices
        super().__init__(self.prices)

    def get_price(self,
                  color: Optional[Color] = ...,
                  platform: Optional[Platform] = ...,
                  blueprint: Optional[Blueprint] = ...) -> Tuple[Price, CraftingCost]: ...
