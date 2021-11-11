from rl_data_utils.__others import _regex_found
from rl_data_utils.utils.item.serie.regexs import *


def contains_accelerator_series(serie: str) -> bool:
    return _regex_found(CONTAINS_ACCELERATOR_SERIES, serie)


def contains_beach_blast_series(serie: str) -> bool:
    return _regex_found(CONTAINS_BEACH_BLAST_SERIES, serie)


def contains_bonus_gift(serie: str) -> bool:
    return _regex_found(CONTAINS_BONUS_GIFT, serie)


def contains_champions_1_series(serie: str) -> bool:
    return _regex_found(CONTAINS_CHAMPIONS_1_SERIES, serie)


def contains_champions_2_series(serie: str) -> bool:
    return _regex_found(CONTAINS_CHAMPIONS_2_SERIES, serie)


def contains_champions_3_series(serie: str) -> bool:
    return _regex_found(CONTAINS_CHAMPIONS_3_SERIES, serie)


def contains_champions_4_series(serie: str) -> bool:
    return _regex_found(CONTAINS_CHAMPIONS_4_SERIES, serie)


def contains_elevation_series(serie: str) -> bool:
    return _regex_found(CONTAINS_ELEVATION_SERIES, serie)


def contains_ferocity_series(serie: str) -> bool:
    return _regex_found(CONTAINS_FEROCITY_SERIES, serie)


def contains_golden_egg_2018(serie: str) -> bool:
    return _regex_found(CONTAINS_GOLDEN_EGG_2018, serie)


def contains_golden_egg_2019(serie: str) -> bool:
    return _regex_found(CONTAINS_GOLDEN_EGG_2019, serie)


def contains_golden_egg_2020(serie: str) -> bool:
    return _regex_found(CONTAINS_GOLDEN_EGG_2020, serie)


def contains_golden_gift_2018(serie: str) -> bool:
    return _regex_found(CONTAINS_GOLDEN_GIFT_2018, serie)


def contains_golden_gift_2019(serie: str) -> bool:
    return _regex_found(CONTAINS_GOLDEN_GIFT_2019, serie)


def contains_golden_gift_2020(serie: str) -> bool:
    return _regex_found(CONTAINS_GOLDEN_GIFT_2020, serie)


def contains_golden_lantern_2020(serie: str) -> bool:
    return _regex_found(CONTAINS_GOLDEN_LANTERN_2020, serie)


def contains_golden_lantern_2021(serie: str) -> bool:
    return _regex_found(CONTAINS_GOLDEN_LANTERN_2021, serie)


def contains_golden_pumpkin_2018(serie: str) -> bool:
    return _regex_found(CONTAINS_GOLDEN_PUMPKIN_2018, serie)


def contains_golden_pumpkin_2019(serie: str) -> bool:
    return _regex_found(CONTAINS_GOLDEN_PUMPKIN_2019, serie)


def contains_golden_pumpkin_2020(serie: str) -> bool:
    return _regex_found(CONTAINS_GOLDEN_PUMPKIN_2020, serie)


def contains_haunted_hallows_series(serie: str) -> bool:
    return _regex_found(CONTAINS_HAUNTED_HALLOWS_SERIES, serie)


def contains_impact_series(serie: str) -> bool:
    return _regex_found(CONTAINS_IMPACT_SERIES, serie)


def contains_nitro_series(serie: str) -> bool:
    return _regex_found(CONTAINS_NITRO_SERIES, serie)


def contains_overdrive_series(serie: str) -> bool:
    return _regex_found(CONTAINS_OVERDRIVE_SERIES, serie)


def contains_players_choice_series(serie: str) -> bool:
    return _regex_found(CONTAINS_PLAYERS_CHOICE_SERIES, serie)


def contains_secret_santa_series(serie: str) -> bool:
    return _regex_found(CONTAINS_SECRET_SANTA_SERIES, serie)


def contains_spring_fever_series(serie: str) -> bool:
    return _regex_found(CONTAINS_SPRING_FEVER_SERIES, serie)


def contains_totally_awesome_series(serie: str) -> bool:
    return _regex_found(CONTAINS_TOTALLY_AWESOME_SERIES, serie)


def contains_triumph_series(serie: str) -> bool:
    return _regex_found(CONTAINS_TRIUMPH_SERIES, serie)


def contains_turbo_series(serie: str) -> bool:
    return _regex_found(CONTAINS_TURBO_SERIES, serie)


def contains_velocity_series(serie: str) -> bool:
    return _regex_found(CONTAINS_VELOCITY_SERIES, serie)


def contains_victory_series(serie: str) -> bool:
    return _regex_found(CONTAINS_VICTORY_SERIES, serie)


def contains_vindicator_series(serie: str) -> bool:
    return _regex_found(CONTAINS_VINDICATOR_SERIES, serie)


def contains_zephyr_series(serie: str) -> bool:
    return _regex_found(CONTAINS_ZEPHYR_SERIES, serie)


CONTAINS_FUNCTIONS = [contains_accelerator_series, contains_beach_blast_series, contains_bonus_gift,
                      contains_champions_1_series,
                      contains_champions_2_series, contains_champions_3_series, contains_champions_4_series,
                      contains_elevation_series,
                      contains_ferocity_series, contains_golden_egg_2018, contains_golden_egg_2019,
                      contains_golden_egg_2020,
                      contains_golden_gift_2018, contains_golden_gift_2019, contains_golden_gift_2020,
                      contains_golden_lantern_2020,
                      contains_golden_lantern_2021, contains_golden_pumpkin_2018, contains_golden_pumpkin_2019,
                      contains_golden_pumpkin_2020,
                      contains_haunted_hallows_series, contains_impact_series, contains_nitro_series,
                      contains_overdrive_series,
                      contains_players_choice_series, contains_secret_santa_series, contains_spring_fever_series,
                      contains_totally_awesome_series,
                      contains_triumph_series, contains_turbo_series, contains_velocity_series, contains_victory_series,
                      contains_vindicator_series,
                      contains_zephyr_series]
