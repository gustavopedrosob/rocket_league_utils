from functools import lru_cache
from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.item.serie.regexs import *


@lru_cache
def is_accelerator_series(serie: str) -> bool:
    return _regex_found(IS_ACCELERATOR_SERIES, serie)


@lru_cache
def is_beach_blast_series(serie: str) -> bool:
    return _regex_found(IS_BEACH_BLAST_SERIES, serie)


@lru_cache
def is_bonus_gift(serie: str) -> bool:
    return _regex_found(IS_BONUS_GIFT, serie)


@lru_cache
def is_champions_1_series(serie: str) -> bool:
    return _regex_found(IS_CHAMPIONS_1_SERIES, serie)


@lru_cache
def is_champions_2_series(serie: str) -> bool:
    return _regex_found(IS_CHAMPIONS_2_SERIES, serie)


@lru_cache
def is_champions_3_series(serie: str) -> bool:
    return _regex_found(IS_CHAMPIONS_3_SERIES, serie)


@lru_cache
def is_champions_4_series(serie: str) -> bool:
    return _regex_found(IS_CHAMPIONS_4_SERIES, serie)


@lru_cache
def is_elevation_series(serie: str) -> bool:
    return _regex_found(IS_ELEVATION_SERIES, serie)


@lru_cache
def is_ferocity_series(serie: str) -> bool:
    return _regex_found(IS_FEROCITY_SERIES, serie)


@lru_cache
def is_golden_egg_2018(serie: str) -> bool:
    return _regex_found(IS_GOLDEN_EGG_2018, serie)


@lru_cache
def is_golden_egg_2019(serie: str) -> bool:
    return _regex_found(IS_GOLDEN_EGG_2019, serie)


@lru_cache
def is_golden_egg_2020(serie: str) -> bool:
    return _regex_found(IS_GOLDEN_EGG_2020, serie)


@lru_cache
def is_golden_gift_2018(serie: str) -> bool:
    return _regex_found(IS_GOLDEN_GIFT_2018, serie)


@lru_cache
def is_golden_gift_2019(serie: str) -> bool:
    return _regex_found(IS_GOLDEN_GIFT_2019, serie)


@lru_cache
def is_golden_gift_2020(serie: str) -> bool:
    return _regex_found(IS_GOLDEN_GIFT_2020, serie)


@lru_cache
def is_golden_lantern_2020(serie: str) -> bool:
    return _regex_found(IS_GOLDEN_LANTERN_2020, serie)


@lru_cache
def is_golden_lantern_2021(serie: str) -> bool:
    return _regex_found(IS_GOLDEN_LANTERN_2021, serie)


@lru_cache
def is_golden_pumpkin_2018(serie: str) -> bool:
    return _regex_found(IS_GOLDEN_PUMPKIN_2018, serie)


@lru_cache
def is_golden_pumpkin_2019(serie: str) -> bool:
    return _regex_found(IS_GOLDEN_PUMPKIN_2019, serie)


@lru_cache
def is_golden_pumpkin_2020(serie: str) -> bool:
    return _regex_found(IS_GOLDEN_PUMPKIN_2020, serie)


@lru_cache
def is_haunted_hallows_series(serie: str) -> bool:
    return _regex_found(IS_HAUNTED_HALLOWS_SERIES, serie)


@lru_cache
def is_impact_series(serie: str) -> bool:
    return _regex_found(IS_IMPACT_SERIES, serie)


@lru_cache
def is_nitro_series(serie: str) -> bool:
    return _regex_found(IS_NITRO_SERIES, serie)


@lru_cache
def is_overdrive_series(serie: str) -> bool:
    return _regex_found(IS_OVERDRIVE_SERIES, serie)


@lru_cache
def is_players_choice_series(serie: str) -> bool:
    return _regex_found(IS_PLAYERS_CHOICE_SERIES, serie)


@lru_cache
def is_secret_santa_series(serie: str) -> bool:
    return _regex_found(IS_SECRET_SANTA_SERIES, serie)


@lru_cache
def is_spring_fever_series(serie: str) -> bool:
    return _regex_found(IS_SPRING_FEVER_SERIES, serie)


@lru_cache
def is_totally_awesome_series(serie: str) -> bool:
    return _regex_found(IS_TOTALLY_AWESOME_SERIES, serie)


@lru_cache
def is_triumph_series(serie: str) -> bool:
    return _regex_found(IS_TRIUMPH_SERIES, serie)


@lru_cache
def is_turbo_series(serie: str) -> bool:
    return _regex_found(IS_TURBO_SERIES, serie)


@lru_cache
def is_velocity_series(serie: str) -> bool:
    return _regex_found(IS_VELOCITY_SERIES, serie)


@lru_cache
def is_victory_series(serie: str) -> bool:
    return _regex_found(IS_VICTORY_SERIES, serie)


@lru_cache
def is_vindicator_series(serie: str) -> bool:
    return _regex_found(IS_VINDICATOR_SERIES, serie)


@lru_cache
def is_zephyr_series(serie: str) -> bool:
    return _regex_found(IS_ZEPHYR_SERIES, serie)


IS_FUNCTIONS = [is_accelerator_series, is_beach_blast_series, is_bonus_gift, is_champions_1_series,
                is_champions_2_series, is_champions_3_series, is_champions_4_series, is_elevation_series,
                is_ferocity_series, is_golden_egg_2018, is_golden_egg_2019, is_golden_egg_2020,
                is_golden_gift_2018, is_golden_gift_2019, is_golden_gift_2020, is_golden_lantern_2020,
                is_golden_lantern_2021, is_golden_pumpkin_2018, is_golden_pumpkin_2019, is_golden_pumpkin_2020,
                is_haunted_hallows_series, is_impact_series, is_nitro_series, is_overdrive_series,
                is_players_choice_series, is_secret_santa_series, is_spring_fever_series, is_totally_awesome_series,
                is_triumph_series, is_turbo_series, is_velocity_series, is_victory_series, is_vindicator_series,
                is_zephyr_series]
