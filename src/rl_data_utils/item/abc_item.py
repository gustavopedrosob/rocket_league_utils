from rl_data_utils.color.color import ABCColor
from rl_data_utils.type.type import ABCType
from rl_data_utils.rarity.rarity import ABCRarity
from rl_data_utils.certified.certified import ABCCertified
from rl_data_utils.quantity.quantity import ABCQuantity
from rl_data_utils.name.name import ABCName
from rl_data_utils.item.utils import validate_attributes
from rl_data_utils.__others import filter_container_by_condition


class ABCItem(ABCName, ABCColor, ABCType, ABCRarity, ABCCertified, ABCQuantity):
    def validate(self):
        validate_attributes(self.get_color(), self.get_type(), self.get_rarity(), self.get_certified())

    def __eq__(self, other):
        if isinstance(other, ABCItem):
            return compare_items(self, other)
        else:
            return False


def get_items_by_condition(lamb, items: list[ABCItem]):
    return filter_container_by_condition(lamb, items)


def compare_items(item_1, item_2):
    from rl_data_utils.certified.certified import compare_certificates
    from rl_data_utils.color.color import compare_colors
    from rl_data_utils.name.name import compare_names
    from rl_data_utils.rarity.rarity import compare_rarities
    from rl_data_utils.type.type import compare_types
    for get_function, function in [(ABCItem.get_certified, compare_certificates), (ABCItem.get_color, compare_colors),
                                   (ABCItem.get_name, compare_names), (ABCItem.get_rarity, compare_rarities),
                                   (ABCItem.get_type, compare_types)]:
        item_1_value = get_function(item_1)
        item_2_value = get_function(item_2)
        if item_1_value and item_2_value:
            if not function(item_1_value, item_2_value):
                return False
    return True



