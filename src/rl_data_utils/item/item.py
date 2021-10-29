from rl_data_utils.item.abc_item import ABCItem


class Item(ABCItem):
    def __init__(self, name: str, color: str = "", type_: str = "", rarity: str = "", certified: str = ""):
        self.name = name
        self.color = color
        self.type = type_
        self.rarity = rarity
        self.certified = certified

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
