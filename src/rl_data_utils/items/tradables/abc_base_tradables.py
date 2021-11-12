from abc import ABC, abstractmethod


class ABCBaseTradables(ABC):
    @abstractmethod
    def get_items_by_tradable(self, tradable: bool):
        pass

    @abstractmethod
    def get_items_tradable(self):
        pass

    @abstractmethod
    def get_items_not_tradable(self):
        pass
