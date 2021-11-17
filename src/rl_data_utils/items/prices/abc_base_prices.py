from abc import ABC, abstractmethod


class ABCBasePrices(ABC):
    @abstractmethod
    def get_items_by_price_equal_to(self, price: int):
        pass

    @abstractmethod
    def get_items_by_price_lower_than(self, price: int):
        pass

    @abstractmethod
    def get_items_by_price_higher_than(self, price: int):
        pass

    @abstractmethod
    def get_total_price(self) -> int:
        pass

    @abstractmethod
    def get_total_quantity(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass

    @abstractmethod
    def get_quantities(self):
        pass
