from __future__ import annotations
from rl_data_utils.item.attribute.attribute import Attribute
from rl_data_utils.item.attribute.attribute_info import AttributeInfo


class IntAttribute(Attribute, AttributeInfo):
    attribute_type = int
    undefined_value = 0
