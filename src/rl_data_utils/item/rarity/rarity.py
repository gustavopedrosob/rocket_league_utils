from rl_data_utils.exceptions import RarityNotExists
from rl_data_utils.item.attribute.attribute_dict import AttributeDict
from rl_data_utils.item.attribute.str_attribute import StrAttribute
from rl_data_utils.item.rarity.constants import RARE, VERY_RARE, IMPORT, EXOTIC, BLACK_MARKET, PREMIUM, LIMITED
from rl_data_utils.item.rarity.rarity_info import RarityInfo
from rl_data_utils.item.rarity.regexs import CONTAINS


class Rarity(StrAttribute, RarityInfo):
    _attribute_not_exists_exception = RarityNotExists
    _is_reg = CONTAINS

    # def get_rgba(self, transparency=70) -> list[int]:
    #     result = RGB[self.attribute]
    #     result.append(transparency)
    #     return result


# RGB = AttributeDict(Rarity, {RARE: [116, 151, 235], VERY_RARE: [158, 124, 252], IMPORT: [227, 90, 82],
#                              EXOTIC: [236, 219, 108], BLACK_MARKET: [255, 0, 255], PREMIUM: [107, 241, 174],
#                              LIMITED: [247, 121, 57]})
