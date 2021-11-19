from abc import abstractmethod, ABC
from rl_data_utils.item.item.item_attribute import ItemAttribute


class ABCTradable(ABC, ItemAttribute):
    @abstractmethod
    def get_tradable(self) -> bool:
        pass


class Tradable(ABCTradable):
    def __init__(self, tradable: bool):
        self.tradable = tradable

    def get_tradable(self) -> bool:
        return self.tradable
