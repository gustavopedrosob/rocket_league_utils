from rl_data_utils.items.names.names import ABCNames
from rl_data_utils.items.types.types import ABCTypes
from rl_data_utils.items.colors.colors import ABCColors
from rl_data_utils.items.certificates.certificates import ABCCertificates
from rl_data_utils.items.rarities.rarities import ABCRarities
from rl_data_utils.items.quantities.quantities import ABCQuantities


class Inventory(ABCNames, ABCTypes, ABCColors, ABCCertificates, ABCRarities, ABCQuantities):
    def __init__(self, items):
        self.items = items

    def get_items(self):
        return self.items

    def set_items(self, items):
        self.items = items

