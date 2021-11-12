from re import IGNORECASE
from rl_data_utils.__others import _regex_found
from rl_data_utils.item.serie.serie import ABCSerie
from rl_data_utils.utils.item.serie.series import compare_series, is_serie
from rl_data_utils.utils.items.items.items import get_items_by_condition


def get_items_with_valid_serie(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: is_serie(item.get_serie()), items)


def get_items_by_serie_regex(serie_pattern, items: list[ABCSerie], flags=IGNORECASE):
    return get_items_by_condition(lambda item: _regex_found(serie_pattern, item.get_serie(), flags), items)


def get_items_by_serie(serie: str, items: list[ABCSerie]):
    return get_items_by_condition(lambda item: compare_series(item.get_serie(), serie), items)


def get_items_by_serie_equal_to(serie: str, items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.get_serie() == serie, items)


def get_items_by_serie_contains(serie: str, items: list[ABCSerie]):
    return get_items_by_condition(lambda item: serie in item.get_serie(), items)


def get_series(items: list[ABCSerie]):
    return {item.get_serie() for item in items}


def get_items_accelerator_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_accelerator_series(), items)


def get_items_beach_blast_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_beach_blast_series(), items)


def get_items_bonus_gift(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_bonus_gift(), items)


def get_items_champions_1_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_champions_1_series(), items)


def get_items_champions_2_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_champions_2_series(), items)


def get_items_champions_3_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_champions_3_series(), items)


def get_items_champions_4_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_champions_4_series(), items)


def get_items_elevation_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_elevation_series(), items)


def get_items_ferocity_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_ferocity_series(), items)


def get_items_golden_egg_2018(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_golden_egg_2018(), items)


def get_items_golden_egg_2019(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_golden_egg_2019(), items)


def get_items_golden_egg_2020(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_golden_egg_2020(), items)


def get_items_golden_gift_2018(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_golden_gift_2018(), items)


def get_items_golden_gift_2019(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_golden_gift_2019(), items)


def get_items_golden_gift_2020(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_golden_gift_2020(), items)


def get_items_golden_lantern_2020(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_golden_lantern_2020(), items)


def get_items_golden_lantern_2021(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_golden_lantern_2021(), items)


def get_items_golden_pumpkin_2018(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_golden_pumpkin_2018(), items)


def get_items_golden_pumpkin_2019(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_golden_pumpkin_2019(), items)


def get_items_golden_pumpkin_2020(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_golden_pumpkin_2020(), items)


def get_items_haunted_hallows_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_haunted_hallows_series(), items)


def get_items_impact_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_impact_series(), items)


def get_items_nitro_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_nitro_series(), items)


def get_items_overdrive_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_overdrive_series(), items)


def get_items_players_choice_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_players_choice_series(), items)


def get_items_secret_santa_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_secret_santa_series(), items)


def get_items_spring_fever_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_spring_fever_series(), items)


def get_items_totally_awesome_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_totally_awesome_series(), items)


def get_items_triumph_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_triumph_series(), items)


def get_items_turbo_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_turbo_series(), items)


def get_items_velocity_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_velocity_series(), items)


def get_items_victory_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_victory_series(), items)


def get_items_vindicator_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_vindicator_series(), items)


def get_items_zephyr_series(items: list[ABCSerie]):
    return get_items_by_condition(lambda item: item.is_zephyr_series(), items)
