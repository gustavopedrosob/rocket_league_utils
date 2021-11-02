from abc import ABC, abstractmethod
from rl_data_utils.item.abc_item import get_items_by_condition


class ABCItems(ABC):
    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def set_items(self, items):
        pass

    def __iter__(self):
        for item in self.get_items():
            yield item

    def get_items_by_condition(self, lamb):
        return get_items_by_condition(lamb, self.get_items())

    def add_item(self, item):
        self.get_items().append(item)

    def remove_item(self, item):
        self.get_items().remove(item)

