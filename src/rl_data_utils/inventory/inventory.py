from rl_data_utils.names.names import ABCNames, get_items_by_name
from rl_data_utils.types.types import ABCTypes, get_items_by_type
from rl_data_utils.colors.colors import ABCColors, get_items_by_color
from rl_data_utils.certificates.certificates import ABCCertificates, get_items_by_certified
from rl_data_utils.rarities.rarities import ABCRarities, get_items_by_rarity
from rl_data_utils.quantities.quantities import ABCQuantities
from rl_data_utils.item.item import ABCItem
from rl_data_utils.item.utils import get_attributes_in_string
from rl_data_utils.item.abc_item import get_item_by_index


class ABCInventory(ABCNames, ABCTypes, ABCColors, ABCCertificates, ABCRarities, ABCQuantities):
    def get_item_by(self, name: str, color: str = None, rarity: str = None, type_: str = None, certified: str = None):
        return get_item_by(self.get_items(), name, color, rarity, type_, certified)

    def get_items_by(self, name: str, color: str = None, rarity: str = None, type_: str = None, certified: str = None):
        return get_items_by(self.get_items(), name, color, rarity, type_, certified)

    def get_items_by_string(self, string: str):
        return get_items_by_string(self.get_items(), string)

    def get_item_by_string(self, string: str):
        return get_item_by_string(self.get_items(), string)


class Inventory(ABCInventory):
    def __init__(self, items: list[ABCItem]):
        self.items = items

    def get_items(self):
        return self.items

    def set_items(self, items: list[ABCItem]):
        self.items = items


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
