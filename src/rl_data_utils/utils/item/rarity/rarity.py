from rl_data_utils.__others import AttributesFunctions
from rl_data_utils.exceptions import RarityNotExists, InvalidRaritiesList
from rl_data_utils.utils.item.rarity.constants import RARITIES
from rl_data_utils.utils.item.rarity.contains import CONTAINS_FUNCTIONS
from rl_data_utils.utils.item.rarity.is_functions import IS_FUNCTIONS, is_rare, is_very_rare, is_import, is_exotic, \
    is_black_market, is_premium, is_limited
from rl_data_utils.utils.item.rarity.regexs import CONTAINS_REGEXS


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


def has_rarity(string: str, container: list) -> bool:
    return RaritiesFunctions.has(string, container)


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


def validate_rarities_list(container):
    return RaritiesFunctions.validate_list(container)


def validate_rarity(string):
    return RaritiesFunctions.validate(string)