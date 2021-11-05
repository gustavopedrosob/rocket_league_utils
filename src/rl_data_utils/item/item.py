from rl_data_utils.item.utils import get_attributes_in_string
from rl_data_utils.name.name import ABCName
from rl_data_utils.color.color import ABCColor
from rl_data_utils.type.type import ABCType
from rl_data_utils.rarity.rarity import ABCRarity
from rl_data_utils.certified.certified import ABCCertified
from rl_data_utils.quantity.quantity import ABCQuantity


class Item(ABCName, ABCColor, ABCType, ABCRarity, ABCCertified, ABCQuantity):
    def __init__(self, name: str, color: str = "", type_: str = "", rarity: str = "", certified: str = "",
                 quantity: int = 1):
        self.name = name
        self.color = color
        self.type = type_
        self.rarity = rarity
        self.certified = certified
        self.quantity = quantity

    def get_certified(self):
        return self.certified

    def set_certified(self, certified: str):
        self.certified = certified

    def get_color(self):
        return self.color

    def set_color(self, color: str):
        self.color = color

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_rarity(self):
        return self.rarity

    def set_rarity(self, rarity: str):
        self.rarity = rarity

    def get_type(self):
        return self.type

    def set_type(self, type_: str):
        self.type = type_

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        self.quantity = quantity

    @staticmethod
    def from_string(string: str):
        return Item(**get_attributes_in_string(string))
