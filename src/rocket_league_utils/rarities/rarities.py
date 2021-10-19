from rocket_league_utils.rarities.isandcompare import RarityIsAndCompare
from rocket_league_utils.rarities.is_functions import *
from rocket_league_utils.rarities.constants import *


def is_rarity(string: str) -> bool:
    return RarityIsAndCompare.is_(string)


def compare_rarities(rarity_1: str, rarity_2: str) -> bool:
    return RarityIsAndCompare.compare_(rarity_1, rarity_2)


def get_respective_rarity(rarity: str) -> bool:
    if is_rare(rarity):
        return RARE
    elif is_very_rare(rarity):
        return VERY_RARE
    elif is_import(rarity):
        return IMPORT
    elif is_exotic(rarity):
        return EXOTIC
    elif is_black_market(rarity):
        return BLACK_MARKET
    elif is_premium(rarity):
        return PREMIUM
    elif is_limited(rarity):
        return LIMITED


def get_rgba_rarity(rarity: str):
    if is_rare(rarity):
        return 116, 151, 235, .3
    elif is_very_rare(rarity):
        return 158, 124, 252, .3
    elif is_import(rarity):
        return 227, 90, 82, .3
    elif is_exotic(rarity):
        return 236, 219, 108, .3
    elif is_black_market(rarity):
        return 255, 0, 255, .3
    elif is_premium(rarity):
        return 107, 241, 174, .3
    elif is_limited(rarity):
        return 247, 121, 57, .3


class Rarity:
    def __init__(self, rarity: str):
        self.rarity = rarity

    def is_limited(self) -> bool:
        return is_limited(self.rarity)

    def is_uncommon(self) -> bool:
        return is_uncommon(self.rarity)

    def is_black_market(self) -> bool:
        return is_black_market(self.rarity)

    def is_rare(self) -> bool:
        return is_rare(self.rarity)

    def is_very_rare(self) -> bool:
        return is_very_rare(self.rarity)

    def is_exotic(self) -> bool:
        return is_exotic(self.rarity)

    def is_import(self) -> bool:
        return is_import(self.rarity)

    def is_premium(self) -> bool:
        return is_premium(self.rarity)

    def compare_rarities(self, rarity: str):
        return compare_rarities(self.rarity, rarity)

    def get_respective_rarity(self):
        return get_respective_rarity(self.rarity)

    def get_rgba_rarity(self):
        return get_rgba_rarity(self.rarity)
