from rl_data_utils.item import Rarity
from rl_data_utils.item.attribute.str_list_attribute import StrListAttribute
from rl_data_utils.item.rarity.rarity_info import RarityInfo


class Rarities(StrListAttribute, RarityInfo):
    sub_attribute = Rarity
