from rl_data_utils.__others import _regex_found
from rl_data_utils.rarities.regexs import *


def contains_black_market(rarity: str) -> bool:
    return _regex_found(CONTAINS_BLACK_MARKET, rarity)


def contains_exotic(rarity: str) -> bool:
    return _regex_found(CONTAINS_EXOTIC, rarity)


def contains_import(rarity: str) -> bool:
    return _regex_found(CONTAINS_IMPORT, rarity)


def contains_limited(rarity: str) -> bool:
    return _regex_found(CONTAINS_LIMITED, rarity)


def contains_premium(rarity: str) -> bool:
    return _regex_found(CONTAINS_PREMIUM, rarity)


def contains_rare(rarity: str) -> bool:
    return _regex_found(CONTAINS_RARE, rarity)


def contains_uncommon(rarity: str) -> bool:
    return _regex_found(CONTAINS_UNCOMMON, rarity)


def contains_very_rare(rarity: str) -> bool:
    return _regex_found(CONTAINS_VERY_RARE, rarity)


CONTAINS_FUNCTIONS = [contains_black_market, contains_exotic, contains_import, contains_limited, contains_premium,
                      contains_rare, contains_uncommon, contains_very_rare]
