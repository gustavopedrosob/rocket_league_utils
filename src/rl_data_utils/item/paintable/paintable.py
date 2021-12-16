from typing import Union, Final

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.bool_attribute import BoolAttribute
from rl_data_utils.item.attribute.regex_based_attribute import SetRegexBasedAttribute


class PaintableInfo(AttributeInfo):
    attribute_name: Final[str] = 'paintable'
    order: Final[int] = 10


class Paintable(BoolAttribute, PaintableInfo):
    pass


Paintable.default_value = Paintable.undefined_value

InitializePaintable = Union[Paintable, bool, None]


class HasPaintable(PaintableInfo):
    def __init__(self, paintable: InitializePaintable = None):
        self.paintable: Paintable = paintable

    def get_paintable(self) -> Paintable:
        return self._paintable

    def set_paintable(self, value: SetRegexBasedAttribute):
        self._paintable = Paintable.initialize(value)

    paintable = property(get_paintable, set_paintable)
