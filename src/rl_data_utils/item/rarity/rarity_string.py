from rl_data_utils.exceptions import RarityIsNotInString
from rl_data_utils.item.attribute.attribute_string import AttributeString
from rl_data_utils.item.rarity.rarity_info import RarityInfo
from rl_data_utils.item.rarity.regexs import CONTAINS
from rl_data_utils.item.rarity.rarity import Rarity


class RarityString(AttributeString, RarityInfo):
    attribute_class = Rarity
    contains_reg = CONTAINS
    is_not_in_string_exception = RarityIsNotInString
