from rl_data_utils.item import Rarity
from rl_data_utils.item.attribute.attribute_dict import AttributeDict


class RarityDict(AttributeDict):
    def __init__(self, _dict: dict = None):
        super().__init__(Rarity, _dict)
