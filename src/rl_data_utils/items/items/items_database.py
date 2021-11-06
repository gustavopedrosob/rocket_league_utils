from abc import abstractmethod
from rl_data_utils.utils.item_attributes.item_attributes import get_attributes_in_string
from rl_data_utils.utils.items.items.items import get_item_by_index
from rl_data_utils.item.item.item_data import ABCItemData
from rl_data_utils.items.items.items import ABCItems


class ABCItemsDatabase(ABCItems):
    @abstractmethod
    def get_items(self) -> list[ABCItemData]:
        pass

    def get_items_data_by(self, items=None, **kwargs):
        if items is None:
            items = self.get_items()
        return ABCItems.get_items_by(self, items, **kwargs)

    def get_item_data_by(self, **kwargs):
        return get_item_by_index(self.get_items_data_by(**kwargs))

    def get_items_data_by_string(self, string: str):
        kwargs = get_attributes_in_string(string)
        return self.get_items_data_by(**kwargs)

    def get_item_data_by_string(self, string: str):
        kwargs = get_attributes_in_string(string)
        return self.get_item_data_by(**kwargs)

    def get_items_by(self, **kwargs):
        return [item.to_item() for item in self.get_items_data_by(**kwargs)]
