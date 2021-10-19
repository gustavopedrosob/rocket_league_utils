from rocket_league_utils.colors.colors import Color
from rocket_league_utils.types.types import Type
from rocket_league_utils.rarities.rarities import Rarity
from rocket_league_utils.certificates.certificates import Certified


class Item(Color, Type, Rarity, Certified):
    def __init__(self, color: str = "", type_: str = "", rarity: str = "", certified: str = ""):
        self.color = color
        self.type = type_
        self.rarity = rarity
        self.certified = certified
