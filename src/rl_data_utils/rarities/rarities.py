from rl_data_utils.rarities.is_functions import *
from rl_data_utils.rarities.constants import *
from rl_data_utils.__others import AttributesFunctions
from rl_data_utils.exceptions import RarityNotExists, InvalidRaritiesList
from rl_data_utils.rarities.contains import CONTAINS_FUNCTIONS
from rl_data_utils.rarities.regexs import CONTAINS_REGEXS


class RaritiesFunctions(AttributesFunctions):
    is_functions = IS_FUNCTIONS
    contains_functions = CONTAINS_FUNCTIONS
    contains_regex = CONTAINS_REGEXS
    attribute_not_exists_exception = RarityNotExists
    invalid_attribute_list_exception = InvalidRaritiesList


def all_are_rarities(container):
    return RaritiesFunctions.all_are(container)


def compare_rarities(rarity_1: str, rarity_2: str) -> bool:
    return RaritiesFunctions.compare(rarity_1, rarity_2)


def contains_rarities(string: str):
    return RaritiesFunctions.contains(string)


def contains_rarities_in_list(string: str, container: list) -> bool:
    return RaritiesFunctions.contains_in_list(string, container)


def get_rarity_in_string(string: str) -> str:
    return RaritiesFunctions.get_in_string(string)


def get_respective_rarity(rarity, rarities=RARITIES):
    return RaritiesFunctions.get_respective(rarity, rarities)


def get_rgb_rarity(rarity: str):
    if is_rare(rarity):
        return 116, 151, 235
    elif is_very_rare(rarity):
        return 158, 124, 252
    elif is_import(rarity):
        return 227, 90, 82
    elif is_exotic(rarity):
        return 236, 219, 108
    elif is_black_market(rarity):
        return 255, 0, 255
    elif is_premium(rarity):
        return 107, 241, 174
    elif is_limited(rarity):
        return 247, 121, 57


def is_rarity(string: str) -> bool:
    return RaritiesFunctions.is_(string)


def is_rarity_list(container) -> bool:
    return RaritiesFunctions.validate_list(container)


def validate_rarities_list(container):
    return RaritiesFunctions.validate_list(container)


def validate_rarity(string):
    return RaritiesFunctions.validate(string)


class Rarity:
    def __init__(self, rarity: str):
        self.rarity = rarity

    def get_respective_rarity(self):
        return get_respective_rarity(self.rarity)

    def get_rgba_rarity(self):
        return get_rgba_rarity(self.rarity)

    def is_black_market(self) -> bool:
        return is_black_market(self.rarity)

    def is_exotic(self) -> bool:
        return is_exotic(self.rarity)

    def is_import(self) -> bool:
        return is_import(self.rarity)

    def is_limited(self) -> bool:
        return is_limited(self.rarity)

    def is_premium(self) -> bool:
        return is_premium(self.rarity)

    def is_rare(self) -> bool:
        return is_rare(self.rarity)

    def is_uncommon(self) -> bool:
        return is_uncommon(self.rarity)

    def is_very_rare(self) -> bool:
        return is_very_rare(self.rarity)

    def validate_rarity(self):
        validate_rarity(self.rarity)
