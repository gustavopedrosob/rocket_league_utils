from abc import ABC, abstractmethod
from statistics import mean
from rl_data_utils.item.item.item_attribute import ItemAttribute


class ABCPrice(ABC, ItemAttribute):
    @abstractmethod
    def get_price(self) -> list[int]:
        pass

    def get_average_price(self) -> int:
        return mean(self.get_price())


class Price(ABCPrice):
    def __init__(self, price: list[int]):
        self.price = price

    def get_price(self) -> list[int]:
        return self.price
