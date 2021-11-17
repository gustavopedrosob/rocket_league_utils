from abc import ABC, abstractmethod


class ABCBasePaintables(ABC):
    @abstractmethod
    def get_items_by_paintable(self, paintable: bool):
        pass

    @abstractmethod
    def get_items_paintable(self):
        pass

    @abstractmethod
    def get_items_not_paintable(self):
        pass
