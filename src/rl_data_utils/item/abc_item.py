from rl_data_utils.colors.colors import ABCColor
from rl_data_utils.types.types import ABCType
from rl_data_utils.rarities.rarities import ABCRarity
from rl_data_utils.certificates.certificates import ABCCertified
from rl_data_utils.names.names import ABCName
from rl_data_utils.item.utils import validate_attributes, compare_items


class ABCItem(ABCName, ABCColor, ABCType, ABCRarity, ABCCertified):
    def validate(self):
        validate_attributes(self.get_color(), self.get_type(), self.get_rarity(), self.get_certified())

    def __eq__(self, other):
        if isinstance(other, ABCItem):
            return compare_items(self, other)
        else:
            return False
