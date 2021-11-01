from rl_data_utils.names.names import ABCNames
from rl_data_utils.types.types import ABCTypes
from rl_data_utils.colors.colors import ABCColors
from rl_data_utils.certificates.certificates import ABCCertificates
from rl_data_utils.rarities.rarities import ABCRarities
from rl_data_utils.quantities.quantities import ABCQuantities
from rl_data_utils.item.item import ABCItem
from rl_data_utils.items.abc_items import get_items_by


class Inventory(ABCNames, ABCTypes, ABCColors, ABCCertificates, ABCRarities, ABCQuantities):
    def __init__(self, items: list[ABCItem]):
        self.items = items

    def get_items(self):
        return self.items

    def set_items(self, items: list[ABCItem]):
        self.items = items

    def get_items_by(self, name: str, color=None, rarity=None, type_=None, certified=None):
        return get_items_by(self.get_items(), name, color, rarity, type_, certified)

