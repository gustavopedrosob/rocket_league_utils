from abc import ABC, abstractmethod
from operator import sub, add


class ABCQuantity(ABC):
    @abstractmethod
    def get_quantity(self) -> int:
        pass

    @abstractmethod
    def set_quantity(self, quantity: int):
        pass

    def _operation_math(self, other, operation):
        if isinstance(other, ABCQuantity):
            return operation(self.get_quantity(), other.get_quantity())
        elif isinstance(other, int):
            return operation(self.get_quantity(), other)
        else:
            raise AttributeError()

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def add(self, other):
        return self._operation_math(other, add)

    def sub(self, other):
        return self._operation_math(other, sub)


class Quantity(ABCQuantity):
    def __init__(self, quantity):
        self.quantity = quantity

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        self.quantity = quantity
