from __future__ import annotations

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.bool_attribute import BoolItemAttribute
from rl_data_utils.item.item.constants import PAINTABLE


class PaintableInfo(AttributeInfo):
    identifier = PAINTABLE
    order = 10


class Paintable(BoolItemAttribute, PaintableInfo):
    pass
