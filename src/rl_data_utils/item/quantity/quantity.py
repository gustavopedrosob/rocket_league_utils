from __future__ import annotations

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.positive_int_attribute import PositiveIntItemAttribute
from rl_data_utils.item.item.constants import QUANTITY


class QuantityInfo(AttributeInfo):
    identifier = QUANTITY
    order = -1


class Quantity(QuantityInfo, PositiveIntItemAttribute):
    pass
