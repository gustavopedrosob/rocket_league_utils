from rocket_league_utils.__others import _regex_found


def is_limited(rarity: str) -> bool:
    return "limited" in rarity.lower()


def is_uncommon(rarity: str) -> bool:
    return "uncommon" in rarity.lower()


def is_black_market(rarity: str) -> bool:
    return _regex_found(r"black[_\- ]?market|bm", rarity)


def is_rare(rarity: str) -> bool:
    return "rare" in rarity.lower()


def is_very_rare(rarity: str) -> bool:
    return _regex_found(r"very[_\- ]?rare|vr", rarity)


def is_exotic(rarity: str) -> bool:
    return "exotic" in rarity.lower()


def is_import(rarity: str) -> bool:
    return "import" in rarity.lower()


def is_premium(rarity: str) -> bool:
    return "premium" in rarity.lower()