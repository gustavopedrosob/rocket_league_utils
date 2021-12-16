from typing import Union, Final

from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.bool_attribute import BoolAttribute, SetBoolAttribute


class TradableInfo(AttributeInfo):
    attribute_name: Final[str] = 'tradable'
    order: Final[int] = 9


class Tradable(BoolAttribute, TradableInfo):
    default_value = True


InitializeTradable = Union[Tradable, bool, None]


class HasTradable(TradableInfo):
    def __init__(self, tradable: InitializeTradable = None):
        self.tradable: Tradable = tradable

    def get_tradable(self) -> Tradable:
        return self._tradable

    def set_tradable(self, value: SetBoolAttribute):
        self._tradable = Tradable.initialize(value)

    tradable = property(get_tradable, set_tradable)
