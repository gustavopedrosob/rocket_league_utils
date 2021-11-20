from abc import abstractmethod
from rl_data_utils.utils.item_attributes.item_attributes import get_attributes_in_string
from rl_data_utils.utils.items.items.items import get_item_by_index
from rl_data_utils.item.item.item_data import ItemDataAttribute
from rl_data_utils.items.items.items import Items


class ItemsDatabase(Items):
    @abstractmethod
    def get_items(self) -> list[ItemDataAttribute]:
        pass

    def get_items_data_by(self, **kwargs):
        return Items.get_items_by(self, **kwargs)

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
