from typing import Final, Union

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.int_attribute import SetIntAttribute
from rl_data_utils.item.quantity.credits_quantity import CreditsQuantity


class CraftingCostInfo(AttributeInfo):
    attribute_name: Final[str] = 'crafting_cost'


class CraftingCost(CreditsQuantity):
    def __init__(self, attribute: SetIntAttribute):
        super().__init__(attribute)


InitializeCraftingCost = Union[CraftingCost, int, None]


class HasCraftingCost(CraftingCostInfo):
    def __init__(self, crafting_cost: InitializeCraftingCost = None):
        self.crafting_cost = crafting_cost

    def get_crafting_cost(self):
        return self._crafting_cost

    def set_crafting_cost(self, value: SetIntAttribute):
        self._crafting_cost = CraftingCost.initialize(value)

    crafting_cost = property(get_crafting_cost, set_crafting_cost)
