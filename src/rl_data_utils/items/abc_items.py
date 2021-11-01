from abc import ABC, abstractmethod
from rl_data_utils.item.abc_item import get_items_by_condition
from rl_data_utils.item.utils import get_attributes_in_string
from rl_data_utils.item.abc_item import get_item_by_index
from rl_data_utils.names.names import get_items_by_name
from rl_data_utils.types.types import get_items_by_type
from rl_data_utils.colors.colors import get_items_by_color
from rl_data_utils.certificates.certificates import get_items_by_certified
from rl_data_utils.rarities.rarities import get_items_by_rarity
from rl_data_utils.item.item import ABCItem


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

    @abstractmethod
    def get_items_by(self, name: str, **kwargs):
        pass

    def get_item_by(self, name: str, **kwargs):
        return get_item_by_index(self.get_items_by(name, **kwargs))

    def get_items_by_string(self, string: str):
        kwargs = get_attributes_in_string(string)
        return self.get_items_by(**kwargs)

    def get_item_by_string(self, string: str):
        kwargs = get_attributes_in_string(string)
        return self.get_item_by(**kwargs)


def get_items_by(items: list[ABCItem], name: str, color: str = None, rarity: str = None, type_: str = None,
                 certified: str = None):
    if rarity:
        items = get_items_by_rarity(rarity, items)
    if type_:
        items = get_items_by_type(type_, items)
    if certified:
        items = get_items_by_certified(certified, items)
    if color:
        items = get_items_by_color(color, items)
    return get_items_by_name(name, items)


def get_item_by(items: list[ABCItem], name: str, color: str = None, rarity: str = None, type_: str = None,
                certified: str = None):
    return get_item_by_index(get_items_by(items, name, color, rarity, type_, certified))


def get_items_by_string(items: list[ABCItem], string: str):
    kwargs = get_attributes_in_string(string)
    return get_items_by(items, **kwargs)


def get_item_by_string(items: list[ABCItem], string: str):
    return get_items_by_string(items, string)[0]

