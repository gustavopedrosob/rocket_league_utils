from rl_data_utils.__others import _regex_found
from rl_data_utils.rarity.regexs import *


def is_black_market(rarity: str) -> bool:
    return _regex_found(IS_BLACK_MARKET, rarity)


def is_exotic(rarity: str) -> bool:
    return _regex_found(IS_EXOTIC, rarity)


def is_import(rarity: str) -> bool:
    return _regex_found(IS_IMPORT, rarity)


def is_limited(rarity: str) -> bool:
    return _regex_found(IS_LIMITED, rarity)


def is_premium(rarity: str) -> bool:
    return _regex_found(IS_PREMIUM, rarity)


def is_rare(rarity: str) -> bool:
    return _regex_found(IS_RARE, rarity)


def is_uncommon(rarity: str) -> bool:
    return _regex_found(IS_UNCOMMON, rarity)


def is_very_rare(rarity: str) -> bool:
    return _regex_found(IS_VERY_RARE, rarity)


IS_FUNCTIONS = [is_black_market, is_exotic, is_import, is_limited, is_premium,
                is_rare, is_uncommon, is_very_rare]
