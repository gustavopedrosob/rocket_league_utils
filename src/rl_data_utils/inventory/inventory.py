from rl_data_utils.names.names import ABCNames
from rl_data_utils.types.types import ABCStrTypes
from rl_data_utils.colors.colors import ABCStrColors
from rl_data_utils.certificates.certificates import ABCStrCertificates
from rl_data_utils.rarities.rarities import ABCStrRarities
from rl_data_utils.quantities.quantities import ABCQuantities
from rl_data_utils.item.item import ABCItem
from rl_data_utils.items.abc_items import get_items_by


class Inventory(ABCNames, ABCStrTypes, ABCStrColors, ABCStrCertificates, ABCStrRarities, ABCQuantities):
    def __init__(self, items: list[ABCItem]):
        self.items = items

    def get_items(self):
        return self.items

    def set_items(self, items: list[ABCItem]):
        self.items = items

    def get_items_by(self, name: str, color=None, rarity=None, type_=None, certified=None):
        return get_items_by(self.get_items(), name, color, rarity, type_, certified)

