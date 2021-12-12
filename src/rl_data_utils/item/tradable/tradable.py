from typing import Union, Final

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.bool_attribute import BoolAttribute


class TradableInfo(AttributeInfo):
    attribute_name: Final[str] = 'tradable'
    order: Final[int] = 9


class Tradable(BoolAttribute, TradableInfo):
    default_value = True


InitializeTradable = Union[Tradable, bool, None]
