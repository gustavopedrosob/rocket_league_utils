from abc import abstractmethod, ABC


class ABCBaseQuantities(ABC):
    @abstractmethod
    def get_items_by_quantity_equal_to(self, quantity: int):
        pass

    @abstractmethod
    def get_items_by_quantity_lower_than(self, quantity: int):
        pass

    @abstractmethod
    def get_items_by_quantity_higher_than(self, quantity: int):
        pass

    @abstractmethod
    def get_total_quantity(self) -> int:
        pass

    @abstractmethod
    def get_quantity(self):
        pass

    @abstractmethod
    def get_quantities(self):
        pass
