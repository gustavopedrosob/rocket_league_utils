from rl_data_utils.items.items_search import ABCItemsSearch
from abc import abstractmethod
from rl_data_utils.item.utils import get_attributes_in_string
from rl_data_utils.item.abc_item import get_item_by_index
from rl_data_utils.item.item_data import ABCItemData


class ABCItemsDatabase(ABCItemsSearch):
    @abstractmethod
    def get_items(self) -> list[ABCItemData]:
        pass

    @abstractmethod
    def get_items_data_by(self, name: str, **kwargs):
        pass

    def get_item_data_by(self, name: str, **kwargs):
        return get_item_by_index(self.get_items_data_by(name, **kwargs))

    def get_items_data_by_string(self, string: str):
        kwargs = get_attributes_in_string(string)
        return self.get_items_data_by(**kwargs)

    def get_item_data_by_string(self, string: str):
        kwargs = get_attributes_in_string(string)
        return self.get_item_data_by(**kwargs)

    def get_items_by(self, name: str, **kwargs):
        return [item.to_item() for item in self.get_items()]
