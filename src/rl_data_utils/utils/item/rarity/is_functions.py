from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.item.rarity.regexs import IS_BLACK_MARKET, IS_COMMON, IS_EXOTIC, IS_IMPORT, IS_LEGACY, \
    IS_LIMITED, IS_PREMIUM, IS_RARE, IS_UNCOMMON, IS_VERY_RARE


def is_black_market(rarity: str) -> bool:
    return _regex_found(IS_BLACK_MARKET, rarity)


def is_common(rarity: str) -> bool:
    return _regex_found(IS_COMMON, rarity)


def is_exotic(rarity: str) -> bool:
    return _regex_found(IS_EXOTIC, rarity)


def is_import(rarity: str) -> bool:
    return _regex_found(IS_IMPORT, rarity)


def is_legacy(rarity: str) -> bool:
    return _regex_found(IS_LEGACY, rarity)


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


IS_FUNCTIONS = [is_black_market, is_common, is_exotic, is_import, is_legacy, is_limited, is_premium, is_rare,
                is_uncommon,
                is_very_rare]
