from rl_data_utils.items.names.names import Names
from rl_data_utils.items.types.types import Types
from rl_data_utils.items.colors.colors import Colors
from rl_data_utils.items.certificates.certificates import Certificates
from rl_data_utils.items.rarities.rarities import Rarities
from rl_data_utils.items.quantities.quantities import Quantities


class Inventory(Names, Types, Colors, Certificates, Rarities, Quantities):
    def __init__(self, items):
        self.items = items

    def get_items(self):
        return self.items

    def set_items(self, items):
        self.items = items

