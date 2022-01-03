from rl_data_utils.item.attribute.attribute_info import AttributeInfo
from rl_data_utils.item.attribute.bool_attribute import BoolItemAttribute
from rl_data_utils.item.item.constants import FAVORITE


class FavoriteInfo(AttributeInfo):
    identifier = FAVORITE
    order = 13


class Favorite(BoolItemAttribute, FavoriteInfo):
    pass
