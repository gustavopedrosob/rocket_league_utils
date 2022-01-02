from __future__ import annotations

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.item.constants import CRAFTING_COST
from rl_data_utils.item.quantity.credits_quantity import CreditsQuantity


class CraftingCostInfo(AttributeInfo):
    identifier = CRAFTING_COST


class CraftingCost(CreditsQuantity):
    pass
