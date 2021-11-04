from rl_data_utils.names.names import ABCNames
from rl_data_utils.types.types import ABCStrTypes
from rl_data_utils.colors.colors import ABCStrColors
from rl_data_utils.certificates.certificates import ABCStrCertificates
from rl_data_utils.rarities.rarities import ABCStrRarities
from rl_data_utils.quantities.quantities import ABCQuantities
from rl_data_utils.item.item import ABCItem
from rl_data_utils.items.items_search import ABCItemsSearch


class Inventory(ABCNames, ABCStrTypes, ABCStrColors, ABCStrCertificates, ABCStrRarities, ABCQuantities, ABCItemsSearch):
    def __init__(self, items: list[ABCItem]):
        self.items = items

    def get_items(self):
        return self.items

    def set_items(self, items: list[ABCItem]):
        self.items = items

