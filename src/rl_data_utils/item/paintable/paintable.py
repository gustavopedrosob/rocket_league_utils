from typing import Union, Final

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.bool_attribute import BoolAttribute


class PaintableInfo(AttributeInfo):
    attribute_name: Final[str] = 'paintable'
    order: Final[int] = 10


class Paintable(BoolAttribute, PaintableInfo):
    pass


Paintable.default_value = Paintable.undefined_value

InitializePaintable = Union[Paintable, bool, None]
