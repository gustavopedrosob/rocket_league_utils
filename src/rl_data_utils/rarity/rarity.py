from rl_data_utils.rarity.is_functions import *
from rl_data_utils.rarity.constants import *
from rl_data_utils.__others import AttributesFunctions
from rl_data_utils.exceptions import RarityNotExists, InvalidRaritiesList
from rl_data_utils.rarity.contains import CONTAINS_FUNCTIONS
from rl_data_utils.rarity.regexs import CONTAINS_REGEXS
from abc import ABC, abstractmethod


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


def contains_rarity_in_list(string: str, container: list) -> bool:
    return RaritiesFunctions.contains_in_list(string, container)


def get_rarity_in_string(string: str) -> str:
    return RaritiesFunctions.get_in_string(string)


def get_respective_rarity(rarity, rarities=RARITIES):
    return RaritiesFunctions.get_respective(rarity, rarities)


def get_rgba_rarity(rarity: str, transparency=70):
    if is_rare(rarity):
        return 116, 151, 235, transparency
    elif is_very_rare(rarity):
        return 158, 124, 252, transparency
    elif is_import(rarity):
        return 227, 90, 82, transparency
    elif is_exotic(rarity):
        return 236, 219, 108, transparency
    elif is_black_market(rarity):
        return 255, 0, 255, transparency
    elif is_premium(rarity):
        return 107, 241, 174, transparency
    elif is_limited(rarity):
        return 247, 121, 57, transparency


def is_rarity(string: str) -> bool:
    return RaritiesFunctions.is_(string)


def is_rarity_list(container) -> bool:
    return RaritiesFunctions.validate_list(container)


def validate_rarities_list(container):
    return RaritiesFunctions.validate_list(container)


def validate_rarity(string):
    return RaritiesFunctions.validate(string)


class ABCRarity(ABC):
    def get_respective_rarity(self):
        return get_respective_rarity(self.get_rarity())

    def get_rgba_rarity(self):
        return get_rgba_rarity(self.get_rarity())

    def is_black_market(self) -> bool:
        return is_black_market(self.get_rarity())

    def is_exotic(self) -> bool:
        return is_exotic(self.get_rarity())

    def is_import(self) -> bool:
        return is_import(self.get_rarity())

    def is_limited(self) -> bool:
        return is_limited(self.get_rarity())

    def is_premium(self) -> bool:
        return is_premium(self.get_rarity())

    def is_rare(self) -> bool:
        return is_rare(self.get_rarity())

    def is_uncommon(self) -> bool:
        return is_uncommon(self.get_rarity())

    def is_very_rare(self) -> bool:
        return is_very_rare(self.get_rarity())

    def validate_rarity(self):
        validate_rarity(self.get_rarity())

    def compare_rarities(self, rarity: str):
        return compare_rarities(self.get_rarity(), rarity)

    @abstractmethod
    def get_rarity(self):
        pass

    @abstractmethod
    def set_rarity(self, rarity: str):
        pass


class Rarity(ABCRarity):
    def __init__(self, rarity: str):
        self.rarity = rarity

    def get_rarity(self):
        return self.rarity

    def set_rarity(self, rarity: str):
        self.rarity = rarity
