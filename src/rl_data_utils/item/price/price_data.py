from typing import List, Tuple

from rl_data_utils.item.attribute.list_attribute import ListAttribute
from rl_data_utils.item.blueprint.blueprint import InitializeBlueprint, Blueprint
from rl_data_utils.item.color.color import InitializeColor, Color
from rl_data_utils.item.platform.platform import InitializePlatform, Platform
from rl_data_utils.item.crafting_cost.crafting_cost import CraftingCost
from rl_data_utils.item.price.data_price import DataPrice
from rl_data_utils.item.price.price import Price, PriceInfo


class PriceData(ListAttribute, PriceInfo):
    sub_attribute = DataPrice

    def __init__(self, price_data: List[DataPrice]):
        super(PriceData, self).__init__(price_data)

    def has(self, data_price: DataPrice) -> bool:
        return any(attr.compare(data_price) for attr in self.attribute)

    def get_price(self,
                  color: InitializeColor = None,
                  platform: InitializePlatform = None,
                  blueprint: InitializeBlueprint = None,
                  ) -> Tuple[Price, CraftingCost]:
        color = Color.initialize(color)
        platform = Platform.initialize(platform)
        blueprint = Blueprint.initialize(blueprint)
        data_prices: List[DataPrice] = self.attribute
        for attr in (color, platform, blueprint):
            if not attr.is_undefined():
                data_prices = list(filter(lambda dp: attr.compare(dp.get_attr(attr.attribute_name)), data_prices))
        data_price = data_prices[0]
        return {data_price.price, data_price.crafting_cost}
