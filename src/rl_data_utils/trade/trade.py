from rl_data_utils.items.items.items import ABCItems
from abc import ABC, abstractmethod


class ABCTrade(ABC):
    @abstractmethod
    def get_him_items(self) -> ABCItems:
        pass

    @abstractmethod
    def get_my_items(self) -> ABCItems:
        pass

    @abstractmethod
    def get_my_credits(self) -> int:
        pass

    @abstractmethod
    def get_him_credits(self) -> int:
        pass

    def is_sale(self) -> bool:
        return bool(self.get_him_credits())

    def is_buy(self) -> bool:
        return bool(self.get_my_credits())

    