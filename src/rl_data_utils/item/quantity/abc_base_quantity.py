from abc import ABC, abstractmethod


class ABCBaseQuantity(ABC):
    @abstractmethod
    def get_quantity(self) -> int:
        pass

    @abstractmethod
    def set_quantity(self, quantity: int):
        pass

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def sub(self, other):
        pass
