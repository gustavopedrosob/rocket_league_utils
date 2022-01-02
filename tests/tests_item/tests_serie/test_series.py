import pytest

from rl_data_utils.item.serie.constants import *
from rl_data_utils.item.serie.serie import Series, Serie
from tests_item.tests_serie.test_serie import inventory_series


@pytest.mark.parametrize('serie', [*inventory_series, *SERIES])
def test_has_serie(serie):
    assert Series.from_str_list(SERIES).has(Serie(serie))


@pytest.mark.parametrize('serie', [*inventory_series, *SERIES])
def test_get_respective_serie(serie):
    result = Series.from_str_list(SERIES).get_respective(Serie(serie))
    print(result)


@pytest.mark.parametrize('series', [SERIES])
def test_are_valid_series(series):
    assert Series.from_str_list(series).is_valid()


@pytest.mark.parametrize('series', [SERIES])
def test_has_accelerator_series(series):
    assert Series.from_str_list(series).has(Serie(ACCELERATOR_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_accolade_1_series(series):
    assert Series.from_str_list(series).has(Serie(ACCOLADE_SERIES_1))


@pytest.mark.parametrize('series', [SERIES])
def test_has_accolade_2_series(series):
    assert Series.from_str_list(series).has(Serie(ACCOLADE_SERIES_2))


@pytest.mark.parametrize('series', [SERIES])
def test_has_auriga_series(series):
    assert Series.from_str_list(series).has(Serie(AURIGA_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_beach_blast_series(series):
    assert Series.from_str_list(series).has(Serie(BEACH_BLAST_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_bonus_gift(series):
    assert Series.from_str_list(series).has(Serie(BONUS_GIFT))


@pytest.mark.parametrize('series', [SERIES])
def test_has_champions_1_series(series):
    assert Series.from_str_list(series).has(Serie(CHAMPIONS_1_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_champions_2_series(series):
    assert Series.from_str_list(series).has(Serie(CHAMPIONS_2_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_champions_3_series(series):
    assert Series.from_str_list(series).has(Serie(CHAMPIONS_3_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_champions_4_series(series):
    assert Series.from_str_list(series).has(Serie(CHAMPIONS_4_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_elevation_series(series):
    assert Series.from_str_list(series).has(Serie(ELEVATION_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_ferocity_series(series):
    assert Series.from_str_list(series).has(Serie(FEROCITY_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_egg_2018(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_EGG_2018))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_egg_2019(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_EGG_2019))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_egg_2020(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_EGG_2020))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_gift_2018(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_GIFT_2018))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_gift_2019(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_GIFT_2019))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_gift_2020(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_GIFT_2020))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_lantern_2019(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_LANTERN_2019))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_lantern_2020(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_LANTERN_2020))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_lantern_2021(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_LANTERN_2021))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_pumpkin_2018(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_PUMPKIN_2018))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_pumpkin_2019(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_PUMPKIN_2019))


@pytest.mark.parametrize('series', [SERIES])
def test_has_golden_pumpkin_2020(series):
    assert Series.from_str_list(series).has(Serie(GOLDEN_PUMPKIN_2020))


@pytest.mark.parametrize('series', [SERIES])
def test_has_haunted_hallows_series(series):
    assert Series.from_str_list(series).has(Serie(HAUNTED_HALLOWS_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_ignition_series(series):
    assert Series.from_str_list(series).has(Serie(IGNITION_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_impact_series(series):
    assert Series.from_str_list(series).has(Serie(IMPACT_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_momentum_series(series):
    assert Series.from_str_list(series).has(Serie(MOMENTUM_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_nitro_series(series):
    assert Series.from_str_list(series).has(Serie(NITRO_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_non_crate(series):
    assert Series.from_str_list(series).has(Serie(NON_CRATE))


@pytest.mark.parametrize('series', [SERIES])
def test_has_overdrive_series(series):
    assert Series.from_str_list(series).has(Serie(OVERDRIVE_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_players_choice_series(series):
    assert Series.from_str_list(series).has(Serie(PLAYERS_CHOICE_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_rlcs_reward(series):
    assert Series.from_str_list(series).has(Serie(RLCS_REWARD))


@pytest.mark.parametrize('series', [SERIES])
def test_has_season_1(series):
    assert Series.from_str_list(series).has(Serie(SEASON_1))


@pytest.mark.parametrize('series', [SERIES])
def test_has_secret_santa_series(series):
    assert Series.from_str_list(series).has(Serie(SECRET_SANTA_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_spring_fever_series(series):
    assert Series.from_str_list(series).has(Serie(SPRING_FEVER_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_totally_awesome_series(series):
    assert Series.from_str_list(series).has(Serie(TOTALLY_AWESOME_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_triumph_series(series):
    assert Series.from_str_list(series).has(Serie(TRIUMPH_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_turbo_series(series):
    assert Series.from_str_list(series).has(Serie(TURBO_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_velocity_series(series):
    assert Series.from_str_list(series).has(Serie(VELOCITY_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_victory_series(series):
    assert Series.from_str_list(series).has(Serie(VICTORY_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_vindicator_series(series):
    assert Series.from_str_list(series).has(Serie(VINDICATOR_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_zephyr_series(series):
    assert Series.from_str_list(series).has(Serie(ZEPHYR_SERIES))


@pytest.mark.parametrize('series', [SERIES])
def test_has_wwe_promo_code(series):
    assert Series.from_str_list(series).has(Serie(WWE_PROMO_CODE))
