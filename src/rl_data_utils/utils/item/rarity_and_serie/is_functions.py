from rl_data_utils.utils.item.rarity.is_functions import is_very_rare, is_import, is_exotic, is_rare
from rl_data_utils.utils.item.rarity.rarity import validate_rarity
from rl_data_utils.utils.item.serie.is_functions import is_non_crate
from rl_data_utils.utils.item.serie.series import validate_serie


def is_ncvr(rarity: str, serie: str) -> bool:
    validate_rarity(rarity)
    validate_serie(serie)
    return is_very_rare(rarity) and is_non_crate(serie)


def is_nci(rarity: str, serie: str) -> bool:
    validate_rarity(rarity)
    validate_serie(serie)
    return is_import(rarity) and is_non_crate(serie)


def is_nce(rarity: str, serie: str) -> bool:
    validate_rarity(rarity)
    validate_serie(serie)
    return is_exotic(rarity) and is_non_crate(serie)


def is_ncr(rarity: str, serie: str) -> bool:
    validate_rarity(rarity)
    validate_serie(serie)
    return is_rare(rarity) and is_non_crate(serie)

