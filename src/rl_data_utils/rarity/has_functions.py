from rl_data_utils.rarity.is_functions import *


def has_black_market(rarities: list[str]) -> bool:
    return any([is_black_market(rarity) for rarity in rarities])


def has_exotic(rarities: list[str]) -> bool:
    return any([is_exotic(rarity) for rarity in rarities])


def has_import(rarities: list[str]) -> bool:
    return any([is_import(rarity) for rarity in rarities])


def has_limited(rarities: list[str]) -> bool:
    return any([is_limited(rarity) for rarity in rarities])


def has_premium(rarities: list[str]) -> bool:
    return any([is_premium(rarity) for rarity in rarities])


def has_rare(rarities: list[str]) -> bool:
    return any([is_rare(rarity) for rarity in rarities])


def has_uncommon(rarities: list[str]) -> bool:
    return any([is_uncommon(rarity) for rarity in rarities])


def has_very_rare(rarities: list[str]) -> bool:
    return any([is_very_rare(rarity) for rarity in rarities])

