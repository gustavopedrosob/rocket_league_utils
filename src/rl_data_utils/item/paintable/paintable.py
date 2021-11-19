from abc import ABC, abstractmethod
from rl_data_utils.item.item.item_attribute import ItemAttribute


class ABCPaintable(ABC, ItemAttribute):
    @abstractmethod
    def get_paintable(self) -> bool:
        pass


class Paintable:
    def __init__(self, paintable: bool):
        self.paintable = paintable

    def get_paintable(self):
        return self.paintable
