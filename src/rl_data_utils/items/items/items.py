from abc import ABC, abstractmethod
from rl_data_utils.utils.items.items.items import get_items_by_condition, get_item_by_index
from rl_data_utils.items.certificates.abc_base_certificates import ABCBaseCertificates
from rl_data_utils.items.colors.abc_base_colors import ABCBaseColors
from rl_data_utils.items.rarities.abc_base_rarities import ABCBaseRarities
from rl_data_utils.items.types.abc_base_types import ABCBaseTypes
from rl_data_utils.items.names.abc_base_names import ABCBaseNames
from rl_data_utils.utils.item_attributes.item_attributes import get_attributes_in_string


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

    def get_items_by(self, items=None, **kwargs):
        if items is None:
            items = self.get_items()
        if isinstance(self, ABCBaseCertificates) and 'certified' in kwargs:
            items = self.get_items_by_certified(kwargs['certified'], items)
        if isinstance(self, ABCBaseColors) and 'color' in kwargs:
            items = self.get_items_by_color(kwargs['color'], items)
        if isinstance(self, ABCBaseRarities) and 'rarity' in kwargs:
            items = self.get_items_by_rarity(kwargs['rarity'], items)
        if isinstance(self, ABCBaseTypes) and 'type_' in kwargs:
            items = self.get_items_by_type(kwargs['type_'], items)
        if isinstance(self, ABCBaseNames) and 'name' in kwargs:
            items = self.get_items_by_name(kwargs['name'], items)
        return items

    def get_item_by(self, items=None, index=0, **kwargs):
        return get_item_by_index(self.get_items_by(items, **kwargs), index)

    def get_items_by_string(self, string, items=None):
        kw = get_attributes_in_string(string)
        return self.get_items_by(items, **kw)

    def get_item_by_string(self, string, index=0, items=None):
        return get_item_by_index(self.get_items_by_string(string, items), index)

    def get_items_by_item(self, item, items=None):
        kw = item.item_attributes_to_dict()
        return self.get_items_by(items, **kw)

    def get_item_by_item(self, item, items=None, index=0):
        return get_item_by_index(self.get_items_by_item(item, items), index)
